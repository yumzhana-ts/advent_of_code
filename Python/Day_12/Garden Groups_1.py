from utils import *
from model import *
from helpers import *

def process_map(list):
    plant = Plant(list[0][0][0], 0, 0)
    total = 0
    while True:
        plot = Plot(plant)
        plot.process_parent_list_multiple(list)
        plant = refresh(list, plot.get_area())
        total += plot.set_total()
        if plant is None:
            break
    print(total)

def main():
    list = string_to_list(load_json("Day_12_1/mini_data.json"))
    #list = string_to_list(load_json("Day_12/mini_data.json"))
    process_map(list)
    

if __name__ == "__main__":
    main()