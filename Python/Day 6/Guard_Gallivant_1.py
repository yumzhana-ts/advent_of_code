import json
import os
# TODO: 1. parse user
# TODO: 2. move and mark


def load_map():
    with open("Day 6/map.json", "r") as file:
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


def move(file):
    matrix = file
    i = 0
    wall = False
    while wall is False:
        user = find_user(file)
        line, position = user
        current_position = matrix[line][0][position]
        #print(current_position)
        if current_position == '^':
            while True:
                if line <= 0:
                    wall = True
                    break
                elif matrix[line-1][0][position] != "#":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line-1, position, "^")
                    line -= 1
                elif matrix[line-1][0][position] == "#":
                    matrix = replace_step(matrix, line, position, ">")
                    break
            #nice_print(matrix)
            continue
        elif current_position == '>':
            while True:
                if position + 1 < len(matrix[line][0]) and matrix[line][0][position+1] != "#":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position+1, ">")
                    position += 1
                elif position + 1 >= len(matrix[line][0]):
                    wall = True
                    break
                elif matrix[line][0][position+1] == "#":
                    matrix = replace_step(matrix, line, position, "v")
                    break
            #nice_print(matrix)
            continue
        elif current_position == 'v':
            while True:
                if line + 1 >= len(matrix):
                    wall = True
                    break
                elif line + 1 < len(matrix) and matrix[line+1][0][position] != "#":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line+1, position, "v")
                    line += 1
                elif matrix[line+1][0][position] == "#":
                    matrix = replace_step(matrix, line, position, "<")
                    break
            #nice_print(matrix)
            continue
        elif current_position == '<':
            while True:
                if position == 0:
                    wall = True
                    break
                elif position > 0 and matrix[line][0][position-1] != "#":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position-1, "<")
                    position -= 1
                elif position == 0 or matrix[line][0][position-1] == "#":
                    matrix = replace_step(matrix, line, position, "^")
                    break
            #nice_print(matrix)
            continue
    return matrix

def save_json(data):
    folder_name = "Day 6"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = os.path.join(folder_name, f"map.json")
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

def main():
    user = find_user(load_map())
    line, position = user
    print(find_user(load_map()))
    matrix = move(load_map())
    current_position = matrix[line][0][position]
    print(current_position)
    matrix = replace_step(matrix, 3, 129, "X")
    matrix = replace_step(matrix, 93, 71, ">")
    print(find_user(matrix))
    save_json(matrix)
    result = 0
    for item in matrix:
        result+=item[0].count("X")
    print(result+1)


if __name__ == "__main__":
    main()
