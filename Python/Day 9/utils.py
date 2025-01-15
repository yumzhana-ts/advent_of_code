import json

def load_json(file):
    with open(file,"r") as file:
        return (json.load(file))

def nice_print(list):
    for item in list:
        print(item)

