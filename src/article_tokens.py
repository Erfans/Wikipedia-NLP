import os
import re
import json

import nltk as nltk

nltk.download('punkt')


def normalize_text(text, title):
    # remove the title from the beginning of the text
    if text.startswith(title):
        text = text[len(title):]
    # remove additional tags
    normalized = re.sub(r'<.*?/>', ' ', text)
    # fix single quote problem with nltk
    # https://github.com/nltk/nltk/issues/1995
    normalized = re.sub(r"(^|[^\w])'([\w\(][\w ,\-\(\)]*?\w[\?\.\!\,\)]?)'([^\w]|$)", "\\1' \\2 '\\3", normalized,
                        0, re.MULTILINE)
    # add space to em dash to not consider it as one word
    # this character is not dash - https://www.dictionary.com/e/em-dash/
    normalized = re.sub(r'—', ' — ', normalized)
    # add space to slash
    normalized = re.sub(r'/', ' / ', normalized)
    # remove bullet points
    normalized = re.sub(r'BULLET::::', ' ', normalized)
    # remove section points
    normalized = re.sub(r'Section::::', ' ', normalized)
    # replace multiple empty lines with single line break
    normalized = re.sub(r'\n+', "\\n", normalized)
    # replace many spaces with single space
    normalized = re.sub(r' +', ' ', normalized)
    # remove white spaces from beginning and end
    normalized = normalized.strip()

    return normalized


def normalize_token(input_token):
    # lowercase the token
    normalized = input_token.lower()
    # remove possible spaces
    normalized.strip()
    return normalized


source = '../parsed'
destination = '../article_tokens'
for folder_path in sorted(os.listdir(source)):
    current_folder = os.path.join(source, folder_path)
    if os.path.isdir(current_folder):
        print(current_folder)
        destination_folder = os.path.join(destination, folder_path)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print("Create destination directory. " + destination_folder)

        for file_path in sorted(os.listdir(current_folder)):
            current_file = os.path.join(current_folder, file_path)
            if os.path.isfile(current_file):
                print("-- " + current_file)
                with open(current_file, 'r') as f:
                    with open(os.path.join(destination_folder, file_path), "a+") as out_file:
                        for line in f.readlines():
                            page = json.loads(line)
                            word_bag = {}
                            normalized_text = normalize_text(page['text'], page['title'])
                            tokens = nltk.word_tokenize(normalized_text, language='english')
                            for token in tokens:
                                normalized_token = normalize_token(token)
                                if normalized_token not in word_bag.keys():
                                    word_bag[normalized_token] = 1
                                else:
                                    word_bag[normalized_token] += 1

                            out_file.write(json.dumps({
                                'id': page['id'],
                                'title': page['title'],
                                'words': word_bag
                            }, sort_keys=True) + '\n')
