import json
import os
from move_helper import get_user_position
from run_movement import handle_movement_down, handle_movement_left, handle_movement_right, handle_movement_up
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
        if loop_counter >= max_loops and find_two_ones_rows(matrix):
            #print(f"Infinite loop detected with all moves! Exiting...")
            return True
        elif loop_counter >= max_loops:
            #print(f"Infinite loop detected! Exiting...")
            return False
        line, position, current_position = get_user_position(file, matrix)
        if current_position in direction_handlers:
            handler = direction_handlers[current_position]
            matrix, line, position, wall, i = handler(matrix, line, position, wall, i)
            nice_print(matrix)
            loop_counter += 1
    return False

def process_single_file(folder_name, file_index):
    file_name = os.path.join(folder_name, f"map_{file_index}.json")
    #print(f"Processing file {file_index}...")
    state = move(load_map(file_name))
    return state

def process_files(folder_name, file_count=4822):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    locked_routes = 0
    for i in range(file_count):
        state = process_single_file(folder_name, i)
        if state is True:
            print("Detected loop at:", i)
            locked_routes += 1

    print(f"Number of files with locked_routes: {locked_routes}")