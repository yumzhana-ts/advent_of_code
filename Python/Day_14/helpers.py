from utils import *
from model import *

def visualize(robots, max_y, max_x):
    grid = [[[' '] for _ in range(max_y)] for _ in range(max_x)]
    for robot in robots:
        if grid[robot.get_position().get_y()][robot.get_position().get_x()] == [' ']:
            grid[robot.get_position().get_y()][robot.get_position().get_x()] = [str(1)]
        else:
            grid[robot.get_position().get_y()][robot.get_position().get_x()] = [str(value := 1 + 1)]
    #nice_print(grid, "")
    return(grid)


def count_robot_in_quadrant(data, max_x, max_y):
    end_x = max_x//2
    end_y = max_y//2
    q1 = count_robots(data, 0, end_y-1, 0, end_x-1)
    q2 = count_robots(data, 0, end_y-1, end_x+1, end_x+end_x)
    q3 = count_robots(data, end_y+1, end_y+end_y, end_x+1, end_x+end_x)
    q4 = count_robots(data, end_y+1, end_y+end_y, 0, end_x-1)
    return(q1*q2*q3*q4)


def count_robots(data, start_y, end_y, start_x, end_x):
    total = 0
    #print("Function called with:")
    #print(f"start_y={start_y}, end_y={end_y}, start_x={start_x}, end_x={end_x}")
    y = start_y
    while y <= end_y:
        x = start_x
        while x <= end_x:
            if data[y][x] != [' ']:
                case = data[y][x][0]
                try:
                    total += int(case)
                except ValueError:
                    print(f"Warning: Unable to convert {case} to int.")
            x += 1
        y += 1
    print(total)
    return total