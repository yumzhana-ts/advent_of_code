from utils import *
from helpers import *
from dijkstra_algoritm import *
from map_work import *
from collections import Counter

def data_prep():
    data = load_json("Day_20/data/mini_data.json")
    return [list(row) for row in data]

def load_data():
    return load_json("Day_20/data/output.json")

def count_cheats(data, number):
    counts = Counter(n for n in data if n <= number)
    result = dict(counts)
    print_dict(result)
    total = 0
    for key, values in result.items():
        total+=values
    return(total)

def main():
    grid = data_prep()
    result = shortest_path_algorithm(grid)
    #big_n = 9380 - 100
    mini_n = 84 - 50
    print(count_cheats(load_data(), mini_n))


if __name__ == "__main__":
    main()
