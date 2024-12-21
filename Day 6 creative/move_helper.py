import json

def load_map(filename):
    with open(filename, "r") as file:
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


def get_user_position(file, matrix):
    user = find_user(file)
    line, position = user
    current_position = matrix[line][0][position]
    return line, position, current_position