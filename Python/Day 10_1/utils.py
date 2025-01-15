import json

def load_json(file):
    with open(file,"r") as file:
        return (json.load(file))

def nice_print(list):
    for item in list:
        print(item)

def string_to_list(data):
    result = [[[char] for char in string] for sublist in data for string in sublist]
    return result
