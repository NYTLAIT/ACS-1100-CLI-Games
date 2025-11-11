import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

for i in data["cards"]:
    guess = input(i["q"] + ">")
    
    if guess == i["a"]:
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", i["a"]) 
