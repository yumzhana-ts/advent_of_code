import json
import os
from move_helper import replace_step

def save_json(data, i):
    folder_name = "Day 6 creative/big"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = os.path.join(folder_name, f"map_{i}.json")
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

def crazy_mind_up(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, "^")
    fuck = replace_step(matrix, line-1, position, "#")
    save_json(fuck,i)

def crazy_mind_right(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, ">")
    fuck = replace_step(matrix, line, position+1, "#")
    save_json(fuck,i)
    
def crazy_mind_down(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, "v")
    fuck = replace_step(matrix, line+1, position, "#")
    save_json(fuck,i)

def crazy_mind_left(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, "<")
    fuck = replace_step(matrix, line, position-1, "#")
    save_json(fuck,i)