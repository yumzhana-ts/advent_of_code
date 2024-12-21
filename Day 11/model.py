class Stone:
    def __init__(self, number):
        self.number = number

    def set_one(self):
        self.number = 1 # Creating a new Stone with number 1
        return self
    
    def set_two_stones(self, length):
        string = str(self.number)
        stone_len = (length + 1) // 2 
        first_stone = string[:stone_len]
        second_stone = string[stone_len:]
        new_stone1 = Stone(int(first_stone))
        new_stone2 = Stone(int(second_stone))
        return new_stone1, new_stone2

    def set_multiplied(self):
        self.number *= 2024
        return self
    
    def get_number_length(self):
        string = str(self.number)
        return len(string)
    
    def get_value(self):
        return self.number

    def __repr__(self):
        return f"{self.number}"


def blink(number):
    number_length = number.get_number_length()
    if number.get_value() == 0:
        return number.set_one()
    elif number_length % 2 == 0:
        return number.set_two_stones(number_length)
    else:
        return number.set_multiplied()

