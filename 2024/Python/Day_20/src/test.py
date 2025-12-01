from utils import *
from helpers import *
from dijkstra_algoritm import *
from map_work import *
from collections import Counter

def data_prep():
    data = load_json("Day_20/data/big_data.json")
    return [list(row) for row in data]

def main():
    grid = data_prep()
    total = 0
    for items in grid:
        for item in items:
            if item == "#":
                total+=1
    print(total)

if __name__ == "__main__":
    main()
