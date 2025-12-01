def check_range(x, y, data):
    max_x = len(data[0])
    max_y = len(data)
    in_range = 0 <= x < max_x and 0 <= y < max_y
    #print(f"check_range: x={x}, y={y}, max_x={max_x}, max_y={max_y}, in_range={in_range}")
    return in_range

def get_right(y, x, data):
    move_y, move_x = y, x + 1
    #print(f"get_right: start at ({y}, {x}), move to ({move_y}, {move_x})")
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[y][x][0])
        #print(f"get_right: value at ({y}, {x}) = {data[y][x]}, value at ({move_y}, {move_x}) = {data[move_y][move_x]}, diff = {diff}")
        if diff == 1:
            return [move_y, move_x]
    return None

def get_left(y, x, data):
    move_y, move_x = y, x - 1
    #print(f"get_left: start at ({y}, {x}), move to ({move_y}, {move_x})")
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[y][x][0])
        #print(f"get_left: value at ({y}, {x}) = {data[y][x]}, value at ({move_y}, {move_x}) = {data[move_y][move_x]}, diff = {diff}")
        if diff == 1:
            return [move_y, move_x]
    return None

def get_up(y, x, data):
    move_y, move_x = y - 1, x
    #print(f"get_up: start at ({y}, {x}), move to ({move_y}, {move_x})")
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[y][x][0])
        #print(f"get_up: value at ({y}, {x}) = {data[y][x]}, value at ({move_y}, {move_x}) = {data[move_y][move_x]}, diff = {diff}")
        if diff == 1:
            return [move_y, move_x]
    return None

def get_down(y, x, data):
    move_y, move_x = y + 1, x
    #print(f"get_down: start at ({y}, {x}), move to ({move_y}, {move_x})")
    if check_range(move_x, move_y, data):
        diff = int(data[move_y][move_x][0]) - int(data[y][x][0])
        #print(f"get_down: value at ({y}, {x}) = {data[y][x]}, value at ({move_y}, {move_x}) = {data[move_y][move_x]}, diff = {diff}")
        if diff == 1:
            return [move_y, move_x]
    return None

def get_last_step(data, list):
    result = list[-1]
    return result
        

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"