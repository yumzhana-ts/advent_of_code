from utils import *
from helpers import *

def process_doct():
    data = load_json("Day_20/data/mini_data.json")
    walls = []
    for y in range(len(data)):
        x = 0
        while x < (len(data[y])):
            if data[y][x] == "#":
                walls.append((x,y))
            x+=1
    #wall_results = {}
    #for wall in walls:
    #    y, x = wall
    #    wall_directions = []
    #    for direction, (dx_dir, dy_dir) in DIRECTIONS.items():
    #        nx, ny = x + dx_dir, y + dy_dir
    #        if check_range_ww(nx, ny, data) == True:
    #            wall_directions.append((ny, nx))
    #    # Convert tuple (y, x) to a string to use as a key
    #    wall_results[y,x] = wall_directions
    return walls

def main():
    dict = process_doct()
    for key, values in dict.items():
        print(f"{key}")
        for val in values:
            print(list(val))
    

if __name__ == "__main__":
    main()