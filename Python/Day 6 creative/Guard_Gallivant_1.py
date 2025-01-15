import json
# TODO: 1. parse user
# TODO: 2. move and mark


def load_map():
    with open("Day 6 creative/mini/map_0.json", "r") as file:
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
        print("starting loop")
        user = find_user(file)
        line, position = user
        current_position = matrix[line][0][position]
        print(current_position)
        if current_position == '^':
            while True:
                if line <= 0:
                    wall = True
                    break
                elif matrix[line-1][0][position] != "#" and matrix[line-1][0][position] != ".":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line-1, position, "^")
                    print("i am here")
                    line -= 1
                elif matrix[line-1][0][position] == "#" or matrix[line-1][0][position] == ".":
                    matrix = replace_step(matrix, line, position, ">")
                    print("i am here")
                    break
            nice_print(matrix)
            print("continue loop")
            continue
        elif current_position == '>':
            print("i am here")
            while True:
                if position + 1 < len(matrix[line][0]) and matrix[line][0][position+1] != "#" and matrix[line][0][position+1] != ".":
                    print("i am here")
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position+1, ">")
                    position += 1
                elif position + 1 >= len(matrix[line][0]):
                    wall = True
                    break
                elif matrix[line][0][position+1] == "#" or matrix[line][0][position+1] == ".":
                    matrix = replace_step(matrix, line, position, "v")
                    break
            nice_print(matrix)
            continue
        elif current_position == 'v':
            while True:
                if line + 1 >= len(matrix):
                    wall = True
                    break
                elif line + 1 < len(matrix) and matrix[line+1][0][position] != "#" and matrix[line+1][0][position] != ".":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line+1, position, "v")
                    line += 1
                elif matrix[line+1][0][position] == "#" or matrix[line+1][0][position] == ".":
                    matrix = replace_step(matrix, line, position, "<")
                    break
            nice_print(matrix)
            continue
        elif current_position == '<':
            while True:
                if position == 0:
                    wall = True
                    break
                elif position > 0 and matrix[line][0][position-1] != "#" and matrix[line][0][position-1] != ".":
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position-1, "<")
                    position -= 1
                elif position == 0 or matrix[line][0][position-1] == "#" or matrix[line][0][position-1] == "#":
                    matrix = replace_step(matrix, line, position, "^")
                    break
            nice_print(matrix)
            continue
    return matrix

def main():
    matrix = move(load_map())
    result = 0
    for item in matrix:
        result+=item[0].count("X")
    print(result+1)


if __name__ == "__main__":
    main()
