from model import *
from utils import *
from helpers import *


def process_data(data):
    robots = []
    for item in data:
        position = Coordinate(item[0][0],item[0][1])
        velocity = Coordinate(item[1][0],item[1][1])
        robots.append(Robot(position, velocity))
    return robots


def main():
    data = load_json("Day_14/data.json")
    robots = process_data(data)
    max_x, max_y = 101, 103
    visualize(robots, max_x, max_y)
    for _ in range(100):
        for robot in robots:
            robot.step(max_x, max_y)
    grid = visualize(robots, max_x, max_y)
    print(count_robot_in_quadrant(grid, max_x, max_y))
    li = nice_print(grid, "t")
    
    

if __name__ == "__main__":
    main()
