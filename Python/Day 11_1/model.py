from functools import lru_cache

class Stone:
    def __init__(self, number):
        self.number = number

    def set_one(self):
        return Stone(1)

    def set_two_stones(self, length):
        string = str(self.number)
        stone_len = (length + 1) // 2 
        first_stone = string[:stone_len]
        second_stone = string[stone_len:]
        new_stone1 = Stone(int(first_stone))
        new_stone2 = Stone(int(second_stone))
        return new_stone1, new_stone2
    
    def set_multiplied(self):
        return Stone(self.number * 2024)
    
    def get_number_length(self):
        string = str(self.number)
        return len(string)
    
    def get_value(self):
        return self.number

    def __repr__(self):
        return f"{self.number}"

@lru_cache
def blink(stone):
    number_length = stone.get_number_length()
    if stone.get_value() == 0:
        return stone.set_one()
    elif number_length % 2 == 0:
        new_stone1, new_stone2 = stone.set_two_stones(number_length)
        return new_stone1, new_stone2
    else:
        return stone.set_multiplied()