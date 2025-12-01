from model import *
from utils import *
from helper import *

def swap_box(grid,box,x, y):
    x_max = len(grid[0])
    y_max = len(grid)
    box.set_position(Coordinate(x, y, x_max, y_max ))

def box_movement(box, map, move, grid, x, y):
    directions = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
    }
    dx, dy = directions[move]
    if check_boxes(max, x, y, grid, move) != False:
        b_x, b_y = check_boxes(max, x, y, grid, move)
        if abs(b_x - x) > 0:
            number = abs(b_x - x)//2
        elif abs(b_y - y) > 0:
            number = abs(b_y - y)//2
        dx, dy = 0, 0
        for _ in range(2):
            bigbox = map.is_box(box.get_boxes()[0].get_position().get_x() + dx, box.get_boxes()[0].get_position().get_y() + dy)
            bigbox.step(move)
            dx, dy = directions[move]
        #swap_box(grid, box, b_x, b_y)
        map.robot.step(move)
    else:
        box.step(['-'])
    
def single_move(map, move, grid):
    directions = {
        '>': (1, 0),
        '<': (-1, 0),
        'v': (0, 1),
        '^': (0, -1)
    }
    dx, dy = directions[move]
    robot_position_x, robot_position_y = map.robot.get_position().get_x(), map.robot.get_position().get_y()
    if move == ''
    if check_box_position(map, robot_position_x,  robot_position_y,  grid, move,['[']) != False:
        x, y = check_box_position(map, robot_position_x, robot_position_y, grid, move, ['['])
        box = map.is_box(x, y)
        if check_box_position(map, x + dx, y + dy, grid, move, ['[']) != False:
            box_movement(box, map, move, grid, x + dx, y + dy)
        elif check_box_position(map, x + dx, y + dy, grid, move, ['#']) != False:
            box.step(['-'])
        elif check_box_position(map, x + dx, y + dy, grid, move, [' ']) != False:
            box.step(move)
            map.robot.step(move)
    else:
        if check_box_position(map, robot_position_x, robot_position_y, grid, move, ['#']) != False:
            map.robot.step(['-'])
        else:
            map.robot.step(move)
    grid = visualise(grid, map)
    return grid
        
def main():
    data = string_to_list(load_json("Day_15_1/mini_data.json"))
    #nice_print(data, "")
    map = make_map(data)
    grid = visualise(data, map)
    moves = [">"]
    for index, move in enumerate(moves):
        print(f"Step {index + 1}: Executing move '{move}'")
        grid = single_move(map, move, grid)
        #print(f"Grid after move {index + 1}: {grid}")
    #result = 0
    #for box in map.box:
    #    result+=100 * box.get_position().get_y() + box.get_position().get_x()
    #print(result)




if __name__ == "__main__":
    main()