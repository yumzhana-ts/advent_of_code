from utils import *


class Map:
    def __init__(self, reindeer = None, space = None, wall = None, exit_point = None):
        self.reindeer = reindeer
        self.exit_point = exit_point
        self.space = space
        self.wall = wall

    def get_reindeers(self):
        return self.reindeer

    def get_spaces(self):
        return self.space

    def get_walls(self):
        return self.wall


class Space:
    def __init__(self, position, right = None, left= None, up= None, down= None):
        self.position = position
        self.right = right
        self.left = left
        self.up = up
        self.down = down

    def get_position(self):
        return self.position

    def set_right(self, right):
        self.right = right
    
    def set_left(self, left):
        self.left = left
    
    def set_up(self, up):
        self.up = up
    
    def set_down(self, down):
        self.down = down
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def get_up(self):
        return self.up
    
    def get_down(self):
        return self.down
    
    def __repr__(self) -> str:
        return f"[Space: Position={self.position}]"

    def is_space(self, x, y):
        return self.position.is_equal(x, y)


class Reindeer:
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def step(self, move):
        self.position.set_move(move)

    def set_right(self, right):
        self.right = right
    
    def set_left(self, left):
        self.left = left
    
    def set_up(self, up):
        self.up = up
    
    def set_down(self, down):
        self.down = down
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def get_up(self):
        return self.up
    
    def get_down(self):
        return self.down

    def __repr__(self) -> str:
        return f"[Reindeer: Position={self.position}]"


class Exit:
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def step(self, move):
        self.position.set_move(move)

    def __repr__(self) -> str:
        return f"[Exit: Position={self.position}]"


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
    def __init__(self, x, y, x_max = None, y_max = None):
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
            print(f"{GREEN}Action: Moving Up (^) - Result:",
                "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == "v":
            ranged = self.set_y_down()
            print(f"{GREEN}Action: Moving Down (v) - Result:",
                "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == ">":
            ranged = self.set_x_right()
            print(f"{GREEN}Action: Moving Right (>) - Result:",
                "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == "<":
            ranged = self.set_x_left()
            print(f"{GREEN}Action: Moving Left (<) - Result:",
                "Ranged" if ranged else "Not Ranged{RESET}")
        elif move == "-" or ranged == False:
            print(f"{GREEN}Action: No Movement (-)")

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"
    
    
