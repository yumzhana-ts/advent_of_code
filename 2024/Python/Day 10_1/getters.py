from model import *

def check_range(x, y, data):
    max_x = len(data[0])
    max_y = len(data)
    in_range = 0 <= x < max_x and 0 <= y < max_y
    return in_range

def get_right(node, data):
    move_x, move_y = node.x + 1, node.y
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[node.y][node.x][0])
        if diff == 1:
            return Node(move_x, move_y, data[move_y][move_x][0])
    return None

def get_left(node, data):
    move_x, move_y = node.x - 1, node.y
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[node.y][node.x][0])
        if diff == 1:
            return Node(move_x, move_y, data[move_y][move_x][0])
    return None

def get_up(node, data):
    move_x, move_y = node.x, node.y - 1
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[node.y][node.x][0])
        if diff == 1:
            return Node(move_x, move_y, data[move_y][move_x][0])
    return None

def get_down(node, data):
    move_x, move_y = node.x, node.y + 1
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[node.y][node.x][0])
        if diff == 1:
            return Node(move_x, move_y, data[move_y][move_x][0])
    return None