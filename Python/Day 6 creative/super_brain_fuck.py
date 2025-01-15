import json
import os
import threading
# TODO: 1. parse user
# TODO: 2. move and mark


def load_map(name):
    with open(name, "r") as file:
        return (json.load(file))

def find_user(file):
    for i in range(len(file)):
        if file[i][0].find("^") >= 0:
            return ([i, file[i][0].find("^")])
        elif file[i][0].find(">") >= 0:
            return ([i, file[i][0].find(">")])
        elif file[i][0].find("v") >= 0:
            return ([i, file[i][0].find("v")])
        elif file[i][0].find("<") >= 0:
            return ([i, file[i][0].find("<")])

def replace_step(file, line, position, case):
    matrix = [item for item in file]
    matrix[line][0] = matrix[line][0][:position] + \
        case + matrix[line][0][position + 1:]
    return (matrix)

def save_json(data, i):
    folder_name = "Day 6 creative/big"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = os.path.join(folder_name, f"map_{i}.json")
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

def nice_print(matrix):
    for item in matrix:
        print(item)

def crazy_mind_up(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, "^")
    fuck = replace_step(matrix, line-1, position, "#")
    save_json(fuck,i)

def crazy_mind_right(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, ">")
    fuck = replace_step(matrix, line, position+1, "#")
    save_json(fuck,i)
    
def crazy_mind_down(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, "v")
    fuck = replace_step(matrix, line+1, position, "#")
    save_json(fuck,i)

def crazy_mind_left(matrix, i, line, position):
    fuck = replace_step(matrix, line, position, "<")
    fuck = replace_step(matrix, line, position-1, "#")
    save_json(fuck,i)

def move(file):
    matrix = file
    i = 0
    wall = False
    while wall is False:
        print(f"\n--- Step {i} ---")
        print("Finding user position...")
        user = find_user(file)
        line, position = user
        current_position = matrix[line][0][position]

        print(f"User position: line={line}, position={position}, current_position={current_position}")
        print(f"Matrix at start of step {i}:")
        if current_position == '^':
            while True:
                print(f"Moving up from line {line}, position {position}")
                if line <= 0:
                    print("Hit the top edge. Stopping movement.")
                    wall = True
                    break
                elif matrix[line-1][0][position] != "#":
                    i += 1
                    print(f"Open space above. Marking step {i}.")
                    crazy_mind_up(matrix, i, line, position)
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line-1, position, "^")
                    line -= 1
                elif matrix[line-1][0][position] == "#":
                    print("Wall detected above. Stopping movement.")
                    matrix = replace_step(matrix, line, position, ">")
                    break
            continue

        elif current_position == '>':
            while True:
                print(f"Moving right from line {line}, position {position}")
                if position + 1 < len(matrix[line][0]) and matrix[line][0][position+1] != "#":
                    i += 1
                    print(f"Open space to the right. Marking step {i}.")
                    crazy_mind_right(matrix, i, line, position)
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position+1, ">")
                    position += 1
                elif position + 1 >= len(matrix[line][0]):
                    print("Hit the right edge. Stopping movement.")
                    wall = True
                    break
                elif matrix[line][0][position+1] == "#":
                    print("Wall detected to the right. Stopping movement.")
                    matrix = replace_step(matrix, line, position, "v")
                    break
            continue

        elif current_position == 'v':
            while True:
                print(f"Moving down from line {line}, position {position}")
                if line + 1 >= len(matrix):
                    print("Hit the bottom edge. Stopping movement.")
                    wall = True
                    break
                elif line + 1 < len(matrix) and matrix[line+1][0][position] != "#":
                    i += 1
                    print(f"Open space below. Marking step {i}.")
                    crazy_mind_down(matrix, i, line, position)
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line+1, position, "v")
                    line += 1
                elif matrix[line+1][0][position] == "#":
                    print("Wall detected below. Stopping movement.")
                    matrix = replace_step(matrix, line, position, "<")
                    break
            continue

        elif current_position == '<':
            while True:
                print(f"Moving left from line {line}, position {position}")
                if position == 0:
                    print("Hit the left edge. Stopping movement.")
                    wall = True
                    break
                elif position > 0 and matrix[line][0][position-1] != "#":
                    i += 1
                    print(f"Open space to the left. Marking step {i}.")
                    crazy_mind_left(matrix, i, line, position)
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position-1, "<")
                    position -= 1
                elif position == 0 or matrix[line][0][position-1] == "#":
                    print("Wall detected to the left. Stopping movement.")
                    matrix = replace_step(matrix, line, position, "^")
                    break
            continue

    print(f"\nMovement complete. Total steps: {i}")
    print("Final matrix:")
    return matrix

def main():
    folder_name = "Day 6 creative/big"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = os.path.join(folder_name, f"map.json")
    matrix = move(load_map(file_name))
    result = 0
    for item in matrix:
        result+=item[0].count("X")
    print(result+1)


if __name__ == "__main__":
    main()
