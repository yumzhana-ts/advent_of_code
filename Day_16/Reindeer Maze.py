from model import *
from utils import *
from helper import *

def check(data, map, box):
    if box.get_right() != None:
        data[box.get_right().get_position().get_y()][box.get_right().get_position().get_x()] = ["0"]
    if box.get_left() != None:
        data[box.get_left().get_position().get_y()][box.get_left().get_position().get_x()] = ["0"]
    if box.get_up() != None:
        data[box.get_up().get_position().get_y()][box.get_up().get_position().get_x()] = ["0"]
    if box.get_down() != None:
        data[box.get_down().get_position().get_y()][box.get_down().get_position().get_x()] = ["0"]
    nice_print(data, "")


def main():
    data = string_to_list(load_json("Day_16/mini_data.json"))
    nice_print(data, "")
    map = make_map(data)
    visualise(data, map)
    #check(data, map, map.reindeer)
    map.reindeer.step("^")
    visualise(data, map)


if __name__ == "__main__":
    main()