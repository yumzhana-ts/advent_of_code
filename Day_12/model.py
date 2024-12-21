from utils import *
from getters import *

class Plant:
    def __init__(self, type, y, x):
        self.type = type
        self.x = x
        self.y = y
        self.untouched_sides = 0
        self.sides_plants = []
    
    def get_type(self):
        return self.type
    
    def get_untouched_sides(self):
        return self.untouched_sides

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def get_right(self, data):
        move_y, move_x = self.y, self.x + 1
        if check_range(move_x, move_y, data):
            if data[move_y][move_x][0] == self.type:
                return Plant(self.type, move_y, move_x)
        else:
            return None

    def get_left(self, data):
        move_y, move_x = self.y, self.x - 1
        if check_range(move_x, move_y, data):
            if data[move_y][move_x][0] == self.type:
                return Plant(self.type, move_y, move_x)
        return None

    def get_up(self, data):
        move_y, move_x = self.y - 1, self.x
        if check_range(move_x, move_y, data):
            if data[move_y][move_x][0] == self.type:
                return Plant(self.type, move_y, move_x)
        return None

    def get_down(self, data):
        move_y, move_x = self.y + 1, self.x
        if check_range(move_x, move_y, data):
            if data[move_y][move_x][0] == self.type:
                return Plant(self.type, move_y, move_x)
        return None

    def plant_touch(self, data, list):
        right_plant = self.get_right(data)  
        left_plant = self.get_left(data)
        up_plant = self.get_up(data)
        down_plant = self.get_down(data)
        plants = [right_plant, left_plant, up_plant, down_plant]
        valid_plants = [plant for plant in plants if plant is not None]
        self.sides_plants = [plant for plant in plants if plant is None]
        #print(self.sides_plants)
        self.untouched_sides = 4 - len(valid_plants)
        list_coords = {(item.x, item.y) for item in list}
        updated_valid_plants = [plant for plant in valid_plants if (plant.x, plant.y) not in list_coords]
        return updated_valid_plants


    def process_single_parent(self, data, list):
        childs = self.plant_touch(data, list)
        return childs

    def __repr__(self):
        return f"Plant {self.type} [{GREEN}{self.y}{RESET},{GREEN}{self.x}{RESET}]"


class Plot:
    def __init__(self, plant):
        self.type = plant.get_type()
        self.plant = plant
        self.area = [plant]
        self.total = 0
    
    def get_length(self):
        return len(self.area)
    
    def set_total(self):
        return self.get_length() * self.count_untouched()

    def set_new_total(self):
        return self.get_length() * self.count_sides()

    def get_area(self):
        return self.area

    def process_parent_list(self, data, parents):
        all_children = []
        for parent in parents:
            children = parent.process_single_parent(data, self.area)  
            for child in children:
                if child not in self.area:
                    self.area.append(child)
                    all_children.append(child)
        return all_children

    def process_parent_list_multiple(self, data, iterations=5):
        start = self.area
        for i in range(iterations):
            start = self.process_parent_list(data, start)
            if start == []:
                break
        #return current_parents

    def process_length(self):
        list = self.get_area()
        start = list[0].get_y()
        y = 0
        while y < len(list) and list[y].get_y() == start:
            y+=1
        x = len(self.get_area()) // y
        return y, x
    
    def count_untouched(self):
        list = self.get_area()
        total = 0 
        for item in list:
            total += item.get_untouched_sides()
        return total
    
    def get_sides(self):
        list = self.get_area()
        side_y = []
        side_x = []
        for item in list:
            side_x.append(item.get_x())
            side_y.append(item.get_y())
        return side_y, side_x
    
    def count_sides(self):
        y, x = self.get_sides()
        print(y,x)
        start_y = y[0]
        diff_y = 1
        l = []
        for item in y:
            diff_y = abs(start_y - item)+1
        if diff_y == 0:
            diff_y = 1
        if diff_y > 1:
            for item in x:
                if item not in l:
                    l.append(item)
            diff_x = len(l)
        else:
            diff_x = 1
        print(f"y: {diff_y} x: {diff_x}")
        return diff_y * 2 + diff_x * 2

    def __repr__(self) -> str:
        return f"Plot: {RED}{self.type}{RESET} started on row: {GREEN}{self.plant}{RESET}"



