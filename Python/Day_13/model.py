from utils import *
from itertools import product

class Automat:
    def __init__(self, button_a, button_b, prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize
        self.sum
    
    def get_button_a(self):
        return self.button_a

    def get_button_b(self):
        return self.button_b

    def get_prize(self):
        return self.prize
    

    def sum_button_a(self, x, y):
        x += self.button_a.get_x()
        y += self.button_a.get_y()

    def sum_button_b(self, x, y):
        x += self.button_b.get_x()
        y += self.button_b.get_y()

    def sum(self, x, y, button='a'):
        self.sum = lambda x, y, button='a': (
            x + (self.button_a.get_x() if button == 'a' else self.button_b.get_x()),
            y + (self.button_a.get_y() if button == 'a' else self.button_b.get_y()))
   
    def find_combinations(self, part_a, part_b, target):
        #print(f"Initial values - part_a: {part_a}, part_b: {part_b}, target: {target}")
        combinations = []
        for middle in range(target // part_a + 1):
            for n in range(target // part_b + 1):
                result = part_a * middle + part_b * n
                if result == target:
                    combinations.append((middle, n))
                    #print(f"Combination found: middle={middle}, n={n}")
        #if not combinations:
        #    print("No valid combinations found.")
        return combinations
    
    def check_match(self, x, y):
        result = x * self.button_a.get_y() + y * self.button_b.get_y()
        if result == self.prize.get_y():
            return True
        return False


    def __repr__(self) -> str:
        return f"[Automat: Button A={self.button_a}, Button B={self.button_b}, Prize={self.prize}]"


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"