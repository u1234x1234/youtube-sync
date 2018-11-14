import json

with open('config.json', 'r') as in_file:
    config = json.load(in_file)

for item in config:
    print(item)
