from model import *
from utils import *
from helpers import *

tokens = 0

def modify_token(operation):
    global tokens
    if operation == 1:
        tokens += 3
    elif operation == 2:
        tokens += 1
    return tokens

def modify_tokens(a, b):
    global tokens
    for i in range(a):
        modify_token(1)
    for n in range (b):
        modify_token(2)
    return tokens

def process_data(data):
    automats = []
    for item in data:
        coord_a = Coordinate(item[0][1],item[0][2])
        coord_b = Coordinate(item[1][1],item[1][2])
        prize = Coordinate(int(str(10000000000000) + str(item[2][1])), int(str(10000000000000) + str(item[2][2])))
        automats.append(Automat(coord_a, coord_b, prize))
    return automats

def process_automats(automats):
    for i in range(len(automats)):
        list = automats[i].find_combinations(automats[i].get_button_a().get_x(), automats[i].get_button_b().get_x(), automats[i].get_prize().get_x())
        for item in list:
            if automats[i].check_match(item[0], item[1]) == True:
                #print("it's a match")
                modify_tokens(item[0], item[1])
    print(tokens)

def main():
    data = load_json("Day_13/data.json")
    automats = process_data(data)
    nice_print(automats, "Automat")
    process_automats(automats)

            
    

if __name__ == "__main__":
    main()