import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    print(data)