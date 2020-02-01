import json
import re

with open('../results/tokens.json') as tokens_file:
    print("Reading data")
    tokens = json.load(tokens_file)
    print("Filtering data")
    # using isalpha will return true also for characters of other languages
    pattern = re.compile(r'^[a-z]+$')
    filtered = filter(lambda x: pattern.match(x[0]), tokens.items())
    # check qty
    filtered = filter(lambda x: x[1] > 1000, filtered)
    print("Sorting data")
    sorted_list = sorted(filtered, key=lambda x: x[0])

print("Writing data")
# write the file in json format
with open("../results/common_words.json", "a+") as out_file:
    out_file.write(json.dumps([i[0] for i in sorted_list]))
print("Writing is completed")
