from model import *


def check_range(data):
    max_x = len(data[0])
    max_y = len(data)
    return max_x, max_y

def visualise(data, map):
    max_x, max_y = check_range(data)
    grid = [[[' '] for _ in range(max_x)] for _ in range(max_y)]
    walls = map.wall
    boxes = map.box
    robot = map.robot
    for wall in walls:
        grid[wall.get_position().get_y()][wall.get_position().get_x()] = ['#']
    for box in boxes:
        list = box.get_boxes()
        b_r, b_l = list[0], list[1]
        grid[b_r.get_position().get_y()][b_r.get_position().get_x()] = ['[']
        grid[b_l.get_position().get_y()][b_l.get_position().get_x()] = [']']
    grid[robot.get_position().get_y()][robot.get_position().get_x()] = ['@']
    nice_print(grid, "")
    return(grid)


def make_map(data):
    map = Map()
    walls = []
    boxes = []
    x_max, y_max = check_range(data)
    for i in range(len(data)):
        for n in range(len(data[i])):
            if data[i][n] == ["#"]:
                wall = Wall(Coordinate(n, i,  x_max, y_max))
                walls.append(wall)
            elif data[i][n] == ['[']:
                box_r = Box(Coordinate(n, i, x_max, y_max))
                box_l = Box(Coordinate(n+1, i, x_max, y_max))
                box = BigBox([box_r, box_l])
                boxes.append(box)
            elif data[i][n] == ["@"]:
                map.robot = Robot(Coordinate(n, i, x_max, y_max))
    map.wall = walls
    map.box = boxes
    #nice_print(map.wall,"wall")
    #nice_print(map.box, "box")
    #print(map.robot, "robot")
    return map