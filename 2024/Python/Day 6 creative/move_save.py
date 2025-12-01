import json
import os
from move_helper import get_user_position
from save_movement import handle_movement_down, handle_movement_left, handle_movement_right, handle_movement_up
from move_helper import nice_print, load_map

def find_two_ones_rows(matrix):
    
    count = 0
    for row in matrix:
        if row[0].count('1') >= 2:
            count+=1
    return count >= 2   # Return True if there are at least 2 "11"s, otherwise False

def move(file):
    matrix = file
    wall = False
    direction_handlers = {
        '^': handle_movement_up,
        '>': handle_movement_right,
        'v': handle_movement_down,
        '<': handle_movement_left
    }
    i = 0
    max_loops = 5000
    loop_counter = 0
    all_moves = []
    flag = False
    while not wall:
        if loop_counter >= max_loops:
            print(f"Infinite loop detected! Exiting...")
            return False
        line, position, current_position = get_user_position(file, matrix)
        if current_position in direction_handlers:
            handler = direction_handlers[current_position]
            matrix, line, position, wall, i = handler(matrix, line, position, wall, i)
            nice_print(matrix)
            loop_counter += 1
    return False

def process_single_file(folder_name):
    file_name = os.path.join(folder_name, f"map.json")
    move(load_map(file_name))