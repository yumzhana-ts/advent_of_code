from model import *

def check_range(x, y, data):
    max_x = len(data[0])
    max_y = len(data)
    in_range = 0 <= x < max_x and 0 <= y < max_y
    return in_range

def get_right(y, x, data):
    move_y, move_x = y, x + 1
    if check_range(move_x, move_y, data):
        if data[move_y][move_x] == ['.']:
            return Space(Coordinate(move_x, move_y))
    return None

def get_left(y, x, data):
    move_y, move_x = y, x - 1
    if check_range(move_x, move_y, data):
        if data[move_y][move_x] == ['.']:
            return Space(Coordinate(move_x, move_y))
    return None

def get_up(y, x, data):
    move_y, move_x = y - 1, x
    if check_range(move_x, move_y, data):
        if data[move_y][move_x] == ['.']:
            return Space(Coordinate(move_x, move_y))
    return None

def get_down(y, x, data):
    move_y, move_x = y + 1, x
    if check_range(move_x, move_y, data):
        if data[move_y][move_x] == ['.']:
            return Space(Coordinate(move_x, move_y))
    return None