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

def pretty_print_dict(data):
    for key, value in data.items():
        key = key.strip()
        formatted_values = ', '.join(f"[{', '.join(map(str, pair))}]" for pair in value)
        print(f"{key}: {formatted_values}")

def print_routes(routes):
    i = 0
    for route in routes:
        print(f"Route {i}: ", end="")
        for steps in route:
            print(steps, "->", end="")
        print('\n')
        i+=1

def nice_list_print(list, type):
    i = 0
    for item in list:
        i+=1
        print(f"{RED}{type} {i}:{RESET}", item)

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