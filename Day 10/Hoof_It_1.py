from utils import *
from getters import *
from step_check import *
from process_steps import *


def main():
    data = string_to_list(load_json('Day 10/big_data.json'))
    points = starting_points(data)
    i = 0
    mark = 0
    for i in range(len(points)):
        start = [points[i]]
        current_parrents = process_parent_list_multiple(data, start)
        mark += len(current_parrents)
    print(mark)
        

if __name__ == "__main__":
    main()