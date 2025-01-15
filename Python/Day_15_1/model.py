from utils import *

class Map:
    def __init__(self, robot = None, box = None, wall = None):
        self.robot = robot
        self.box = box
        self.wall = wall
    
    def get_robots(self):
        return self.robot

    def get_boxes(self):
        return self.box

    def get_walls(self):
        return self.wall

    def is_box(self, x, y):
        for box in self.box:
            box_r = box.get_boxes()
            if box_r[0].get_position().get_x() == x and box_r[0].get_position().get_y() == y:
                return box

class Robot:
    def __init__(self, position):
        self.position = position
        
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
    
    def step(self, move):
        self.position.set_move(move)

    def __repr__(self) -> str:
        return f"[Robot: Position={self.position}]"

class Box:
    def __init__(self, position):
        self.position = position
        
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
    
    def step(self, move):
        self.position.set_move(move)

    def __repr__(self) -> str:
        return f"[Box: Position={self.position}]"

class BigBox:
    def __init__(self, box):
        self.box = box
        
    def get_boxes(self):
        return self.box

    def set_position(self, boxx):
        self.box = boxx
    
    def step(self, move):
        self.box[0].position.set_move(move)
        self.box[1].position.set_move(move)

    def __repr__(self) -> str:
        return f"[Box: Position={self.Box_r, self.Box_l}]"

class Wall:
    def __init__(self, position):
        self.position = position
        
    def get_position(self):
        return self.position

    def __repr__(self) -> str:
        return f"[Wall: Position={self.position}]"
    
    def is_wall(self, x, y):
        return self.position.is_equal(x, y)
            

class Coordinate:
    def __init__(self, x, y, x_max, y_max):
        self.x = x
        self.y = y
        self.x_max = x_max
        self.y_max = y_max    
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_equal(self, x, y):
        return self.x == x and self.y == y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def check_range(self, x, y):
        return 0 <= x < self.x_max and 0 <= y < self.y_max

    def set_x_left(self):
        if self.check_range(self.x - 1, self.y):
            self.x -= 1
            return True
        return False

    def set_x_right(self):
        if self.check_range(self.x + 1, self.y):
            self.x += 1
            return True
        return False

    def set_y_up(self):
        if self.check_range(self.x, self.y - 1):
            self.y -= 1
            return True
        return False

    def set_y_down(self):
        if self.check_range(self.x, self.y + 1):
            self.y += 1
            return True
        return False
    
    def set_move(self, move):
        ranged = False
        if move == "^":
            ranged = self.set_y_up()
            print(f"{GREEN}Action: Moving Up (^) - Result:", "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == "v":
            ranged = self.set_y_down()
            print(f"{GREEN}Action: Moving Down (v) - Result:", "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == ">":
            ranged = self.set_x_right()
            print(f"{GREEN}Action: Moving Right (>) - Result:", "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == "<":
            ranged = self.set_x_left()
            print(f"{GREEN}Action: Moving Left (<) - Result:", "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == "-" or ranged == False:
            print(f"{GREEN}Action: No Movement (-)")

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"

def check_boxes(map, x, y, grid, move):
    i = 0
    directions = {
        '>': (1, 0),
        '<': (-1, 0),
        'v': (0, 1),
        '^': (0, -1)
    }
    dx, dy = directions[move]
    #print(f"Initial position: ({x}, {y}), move: {move}, case: {case}")
    while True:
        check_x = x + dx * (i + 1)
        check_y = y + dy * (i + 1)
        #print(f"Checking position: ({check_x}, {check_y}), iteration: {i}")
        if not (check_box_position(map, check_x, check_y, grid, move, ['[']) or check_box_position(map, check_x, check_y, grid, move, [']'])):
            print(f"Break condition met at position: ({check_x}, {check_y})")
            break
        i += 1
    final_x = x + dx * (i + 1)
    final_y = y + dy * (i + 1)
    #print(f"Final position to check: ({final_x}, {final_y})")
    result = check_box_position(map, final_x, final_y, grid, move, [' '])
    #print(f"Result of final check_box_position: {result}")
    if result != False:
        final_position = (final_x + dx, final_y + dy)
        print(f"Returning final position: {final_position}")
        return final_position
    else:
        print("Returning False")
        return False

def check_box_position(map, position_x, position_y, grid, move, case):
    if move == "^":
        position_y -= 1
    elif move == "v":
        position_y += 1
    elif move == ">":
        position_x += 1
    elif move == "<":
        position_x -= 1
    else:
        return False
    in_range = check_range(position_x, position_y, grid)
    if in_range:
        match_case = grid[position_y][position_x] == case
        if match_case:
            return position_x, position_y
    return False

