from utils import *
from helpers import *
from dijkstra_algoritm import *
import logging
from itertools import product

logging.basicConfig(level=logging.INFO)

def process_single_press(panel,start, end):
    results = shortest_path_algorithm(panel, start, end)[0]
    result_list = []
    for result in results:
        result.extend("A")
        if result not in result_list:
            result_list.append(result)
    return result_list

def big_press(panel, code):
    start = "A"
    big_combination = []
    for item in code:
        if start == item:
            combinations = [["A"]]
        else:
            combinations = process_single_press(panel, start, item)
            start = item
        big_combination.append(combinations)
    return(big_combination)

def first_robot_single(code, code_panel):
    first_robot = big_press(code_panel, code)
    first_robot_list = process_list(first_robot)
    return first_robot_list

def second_robot_process(code, navigation_panel):
    second_robot = big_press(navigation_panel, code)
    second_robot_list = process_list(second_robot)
    return second_robot_list

def second_robot_mult(codes, navigation_panel):
    big_list = []
    for code in codes:
        big_list+=second_robot_process(code, navigation_panel)
    return big_list

def one_code(code, code_panel, navigation_panel):
    first_robot = first_robot_single(code, code_panel)
    second_robot = second_robot_mult(first_robot, navigation_panel)
    me = second_robot_mult(second_robot, navigation_panel)
    min = 100000000000000
    for item in me:
        if len(item) < min:
            min = len(item)
    return min

def main():
    code_panel = load_json("Day_21/data/code_panel.json")
    navigation_panel = load_json("Day_21/data/navigation_panel.json")
    nice_print(code_panel,"")
    nice_print(navigation_panel,"")
    codes = [["1","7","9","A"]]
    numbers = []
    for code in codes:
        codeg = "".join("".join(char for char in code if char.isdigit()))
        numbers.append(codeg)
    print(numbers)
    i = 0
    total = 0
    for code in codes:
       # total+= one_code(code, code_panel, navigation_panel) * int(numbers[i])
        print(one_code(code, code_panel, navigation_panel))
        #i+=1
    #print(total)

if __name__ == "__main__":
    main()