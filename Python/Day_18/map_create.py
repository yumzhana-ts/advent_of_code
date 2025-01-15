from utils import *
from helpers import *

def example(first, data):
    length = 71
    grid = [['.' for _ in range(length)] for _ in range(length)]
    i = 0
    for _ in range(first):
        grid[data[i][1]][data[i][0]] = "#"
        i+=1
    with open(f'Day_18/maps/grid_{i}.json', 'w') as file:
    	json.dump(grid, file)

def main():
    data = load_json("Day_18/prep.json")
    i = 3029
    print(data[i])
    
    #while i < len(data):
    #    example(i, data)
    #    i+=1
    


if __name__ == "__main__":
    main()
