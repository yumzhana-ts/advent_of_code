import json

def load_json(file):
    with open(file,"r") as file:
        return (json.load(file))

def nice_print(list, type):
    i = 0
    for item in list:
        print(f"{RED}{type} {i}:{RESET}", item)
        i+=1
    print("______________________")
        
def string_to_list(data):
    result = [[[char] for char in string] for sublist in data for string in sublist]
    return result

def nice_list(data):
    result = [[char for char in string] for sublist in data for string in sublist]
    return result

def check_range(x, y, data):
    max_x = len(data[0])
    max_y = len(data)
    in_range = 0 <= x < max_x and 0 <= y < max_y
    return in_range

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
