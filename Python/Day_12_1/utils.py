import json

def load_json(file):
    with open(file,"r") as file:
        return (json.load(file))

def nice_print(list, type):
    i = 0
    for item in list:
        i+=1
        print(f"{RED}{type} {i}:{RESET}", item)
        
def string_to_list(data):
    result = [[[char] for char in string] for sublist in data for string in sublist]
    return result


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
