from model import *
from getters import *

def check_range(data):
    max_x = len(data[0])
    max_y = len(data)
    return max_x, max_y

def visualise(data, map):
    max_x, max_y = check_range(data)
    grid = [[[' '] for _ in range(max_x)] for _ in range(max_y)]
    walls = map.wall
    spaces = map.space
    reindeer = map.reindeer
    exit = map.exit
    for wall in walls:
        grid[wall.get_position().get_y()][wall.get_position().get_x()] = ['#']
    for space in spaces:
        grid[space.get_position().get_y()][space.get_position().get_x()] = ['.']
    grid[reindeer.get_position().get_y()][reindeer.get_position().get_x()] = ['S']
    grid[exit.get_position().get_y()][exit.get_position().get_x()] = ['E']
    nice_print(grid, "")
    return(grid)

def make_map(data):
    map = Map()
    walls = []
    spaces = []
    x_max, y_max = check_range(data)
    for i in range(len(data)):
        for n in range(len(data[i])):
            if data[i][n] == ["#"]:
                wall = Wall(Coordinate(n, i,  x_max, y_max))
                walls.append(wall)
            elif data[i][n] == ['.']:
                space = Space(Coordinate(n, i,  x_max, y_max))
                spaces.append(space)
                save_sides(space, i, n, data)
            elif data[i][n] == ["E"]:
                map.exit = Exit(Coordinate(n, i, x_max, y_max))
            elif data[i][n] == ["S"]:
                map.reindeer = Reindeer(Coordinate(n, i, x_max, y_max))
                save_sides(map.reindeer, i, n, data)
    map.wall = walls
    map.space = spaces
    #nice_print(map.wall,"wall")
    #nice_print(map.space, "space")
    #print(map.reindeer, "reindeer")
    #print(map.exit, "exit")
    return map

def save_sides(space, y, x, data):
    space.set_right(get_right(y, x, data))
    space.set_left(get_left(y, x, data))
    space.set_up(get_up(y, x, data))
    space.set_down(get_down(y, x, data))
    #print(space.get_right(), space.get_left(), space.get_up(), space.get_down())
