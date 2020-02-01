import json
import re
import util

with open('../results/tokens.json') as tokens_file:
    print("Reading data")
    tokens = json.load(tokens_file)
    print("Filtering data")
    # using isalpha will return true also for characters of other languages
    pattern = re.compile(r'^[a-z]+$')
    filtered = filter(lambda x: pattern.match(x[0]), tokens.items())
    print("Sorting data")
    sorted_list = util.sort_tokens_list(filtered)

print("Writing data")
# write the file in json format
with open("../results/words.json", "a+") as out_file:
    out_file.write(json.dumps(dict(sorted_list)))
print("Writing is completed")
