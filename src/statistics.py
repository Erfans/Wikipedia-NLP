import json
import os
import re

import enchant

en = enchant.Dict("en_US")

article_counter = 0
total_tokens = 0
unique_tokens = 0
total_words = 0
unique_words = 0
total_english_words = 0
unique_english_words = 0

word_bag = {}
broken_lines = []

source = '../article_tokens'
print("Reading data")
for folder_path in sorted(os.listdir(source)):
    current_folder = os.path.join(source, folder_path)
    if os.path.isdir(current_folder):
        print(current_folder)

        for file_path in sorted(os.listdir(current_folder)):
            current_file = os.path.join(current_folder, file_path)
            if os.path.isfile(current_file):
                print("-- " + current_file)
                with open(current_file, 'r') as f:

                    for line in f.readlines():
                        if len(line):

                            article_counter += 1

                            try:
                                page = json.loads(line)
                                for w in page['words']:
                                    if w not in word_bag.keys():
                                        word_bag[w] = page['words'][w]
                                    else:
                                        word_bag[w] += page['words'][w]
                            except:
                                broken_lines.append(line)

if len(broken_lines):
    print("===== broken lines =====")
    print(broken_lines)

total_tokens = sum(word_bag.values())
unique_tokens = len(word_bag)
pattern = re.compile(r'^[a-z]+$')
alphabet_words = dict(filter(lambda x: pattern.match(x[0]), word_bag.items()))
english_words = dict(filter(lambda x: en.check(x[0]), word_bag.items()))

print("===== results =====")
print("Number of articles: " + str(article_counter))
print("Total tokens: " + str(sum(word_bag.values())))
print("Unique tokens: " + str(len(word_bag)))
print("Total words: " + str(sum(alphabet_words.values())))
print("Unique words: " + str(len(alphabet_words)))
print("Total english words: " + str(sum(english_words.values())))
print("Unique english words: " + str(len(english_words)))
