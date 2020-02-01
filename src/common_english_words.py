import json
import enchant

en = enchant.Dict("en_US")
with open('../processed/tokens.json') as tokens_file:
    print("Reading data")
    tokens = json.load(tokens_file)
    print("Filtering data")
    # check qty
    filtered = filter(lambda x: x[1] > 1000, tokens.items())
    # check for  alphabetical only tokens
    filtered = filter(lambda x: x[0].isalpha(), filtered)
    # check dictionary
    filtered = filter(lambda x: en.check(x[0]), filtered)
    print("Sorting data")
    sorted_list = sorted(filtered, key=lambda x: x[0])

print("Writing data")
# write the file in json format
with open("../processed/common_english_words.json", "a+") as out_file:
    out_file.write(json.dumps([i[0] for i in sorted_list]))
print("Writing is completed")
