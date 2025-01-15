class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
    
    def get_velocity(self):
        return self.velocity
    
    def step(self, max_x, max_y):
        position_x = (self.velocity.get_x() + self.position.get_x()) % max_x
        position_y = (self.position.get_y() + self.velocity.get_y()) % max_y
        new_positon = Coordinate(position_x,position_y)
        self.set_position(new_positon)

    def __repr__(self) -> str:
        return f"[Robot: Position={self.position}, Velocity={self.velocity}]"

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"