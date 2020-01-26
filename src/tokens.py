import json
import os
import util

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
                            try:
                                page = json.loads(line)
                                for w in page['words']:
                                    if w not in word_bag.keys():
                                        word_bag[w] = page['words'][w]
                                    else:
                                        word_bag[w] += page['words'][w]
                            except:
                                broken_lines.append(line)

print("Writing data")
destination = '../processed/tokens.json'
with open(destination, "a+") as out_file:
    out_file.write(json.dumps(util.sort_tokens_dict(word_bag)))

print("Writing is completed.")
print("Broken lines:")
print(broken_lines)
