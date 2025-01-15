import json
import os

def load_map():
    with open("Day 6/mini/map.json", "r") as file:
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

def nice_print(matrix):
    for item in matrix:
        print(item)

def save_json(data, i):
    folder_name = "Day 6/mini"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = os.path.join(folder_name, f"map_{i}.json")
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

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

def handle_movement_up(matrix, line, position, wall, i):
    while True:
        if line <= 0:
            wall = True
            break
        elif matrix[line-1][0][position] != "#" and matrix[line-1][0][position] != ".":
            crazy_mind_up(matrix, i, line, position)
            i+=1
            matrix = replace_step(matrix, line, position, "|")
            matrix = replace_step(matrix, line-1, position, "^")
            line -= 1
        elif matrix[line-1][0][position] == "#":
            matrix = replace_step(matrix, line, position, ">")
            break
    return matrix, line, position, wall, i

def handle_movement_down(matrix, line, position, wall, i):
    while True:
        if line + 1 >= len(matrix):
            wall = True
            break
        elif line + 1 < len(matrix) and matrix[line+1][0][position] != "#" and matrix[line+1][0][position] != ".":
            crazy_mind_down(matrix, i, line, position)
            i+=1
            matrix = replace_step(matrix, line, position, "|")
            matrix = replace_step(matrix, line+1, position, "v")
            line += 1
        elif matrix[line+1][0][position] == "#":
            matrix = replace_step(matrix, line, position, "<")
            break
    return matrix, line, position, wall, i

def handle_movement_right(matrix, line, position, wall, i):
    while True:
        if position + 1 < len(matrix[line][0]) and matrix[line][0][position+1] != "#" and matrix[line][0][position+1] != ".":
            crazy_mind_right(matrix, i, line, position)
            i+=1
            matrix = replace_step(matrix, line, position, "-")
            matrix = replace_step(matrix, line, position+1, ">")
            position += 1
        elif position + 1 >= len(matrix[line][0]):
            wall = True
            break
        elif matrix[line][0][position+1] == "#":
            matrix = replace_step(matrix, line, position, "v")
            break
    return matrix, line, position, wall, i

def handle_movement_left(matrix, line, position, wall, i):
    while True:
        if position == 0:
            wall = True
            break
        elif position > 0 and matrix[line][0][position-1] != "#" and matrix[line][0][position-1] != ".":
            crazy_mind_left(matrix, i, line, position)
            i+=1
            matrix = replace_step(matrix, line, position, "-")
            matrix = replace_step(matrix, line, position-1, "<")
            position -= 1
        elif position == 0 or matrix[line][0][position-1] == "#":
            matrix = replace_step(matrix, line, position, "^")
            break
    return matrix, line, position, wall, i

def get_user_position(file, matrix):
    user = find_user(file)
    line, position = user
    current_position = matrix[line][0][position]
    return line, position, current_position

def move(file):
    matrix = file
    wall = False
    list_of_positions = []
    direction_handlers = {
        '^': handle_movement_up,
        '>': handle_movement_right,
        'v': handle_movement_down,
        '<': handle_movement_left
    }
    i = 0
    while not wall:
        line, position, current_position = get_user_position(file, matrix)
        if current_position in direction_handlers:
            handler = direction_handlers[current_position]
            matrix, line, position, wall, i = handler(matrix, line, position, wall, i)
            #list_of_positions.append([line, position, current_position])
            nice_print(matrix)
    print(list_of_positions)
    return matrix

def main():
    matrix = move(load_map())
    result = 0
    for item in matrix:
        result+=item[0].count("X")
    print(result+1)


if __name__ == "__main__":
    main()
