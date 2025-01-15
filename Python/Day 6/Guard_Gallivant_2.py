import json
# TODO: 1. directions,
# TODO: 2. 
# TODO: 3. 


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

def create_flood(n, m):
    matrix = [['0'] * n for _ in range(m)]
    return(matrix)

    
def track_and_mark(matrix, row, col, case):
    if matrix[col][row] != '0':
        matrix[col][row] = '+'
    else:
        matrix[col][row] = case
    return matrix

def find_plus_positions(flood):
    positions = []
    for row_index, row in enumerate(flood):
        for col_index, item in enumerate(row):
            if item == '+':
                positions.append([row_index, col_index])
    return positions

def check_elements(list1, list2):
    for num in list1:  # Only check the first two elements
        if num in list2:
            return True
    return False

def move(file):
    matrix = file
    i = 0
    wall = False
    user = find_user(file)
    line_1, position_1 = user
    flood = create_flood(len(matrix[0][0]), len(matrix))
    track_and_mark(flood, position_1, line_1, "|")
    while i < 4:
        user = find_user(file)
        line, position = user
        current_position = matrix[line][0][position]
        print(current_position)
        if current_position == '^':
            while True:
                if line <= 0:
                    wall = True
                    break
                elif  matrix[line-1][0][position] != "#":
                    track_and_mark(flood, position, line-1, "|")
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line-1, position, "^")
                    line -= 1
                elif matrix[line-1][0][position] == "#":
                    matrix = replace_step(matrix, line, position, ">")
                    track_and_mark(flood, position, line, "+")
                    break
            nice_print(matrix)
        elif current_position == '>':
            while True:
                if position + 1 < len(matrix[line][0]) and matrix[line][0][position+1] != "#":
                    track_and_mark(flood, position+1, line, "-")
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position+1, ">")
                    position += 1
                elif position + 1 >= len(matrix[line][0]):
                    wall = True
                    break
                elif matrix[line][0][position+1] == "#":
                    matrix = replace_step(matrix, line, position, "v")
                    track_and_mark(flood, position, line, "+")
                    break
            nice_print(matrix)
        elif current_position == 'v':
            while True:
                if line + 1 >= len(matrix):
                    wall = True
                    break
                elif line + 1 < len(matrix) and matrix[line+1][0][position] != "#":
                    track_and_mark(flood, position, line+1, "|")
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line+1, position, "v")
                    line += 1
                elif matrix[line+1][0][position] == "#":
                    matrix = replace_step(matrix, line, position, "<")
                    track_and_mark(flood, position, line, "+")
                    break
            nice_print(matrix)
        elif current_position == '<':
            while True:
                if position == 0:
                    wall = True
                    break
                elif position > 0 and matrix[line][0][position-1] != "#":
                    track_and_mark(flood, position-1, line, "-")
                    matrix = replace_step(matrix, line, position, "X")
                    matrix = replace_step(matrix, line, position-1, "<")
                    position -= 1
                elif position == 0 or matrix[line][0][position-1] == "#":
                    matrix = replace_step(matrix, line, position, "^")
                    track_and_mark(flood, position, line, "+")
                    break
            nice_print(matrix)
        nice_print(flood)
        #x = find_plus_positions(flood)
        #x.insert(0, [line_1, position_1])
        #nice_print(x)
        #print(check_elements(x[0+i],x[1+i]))
        i+=1    
    nice_print(flood)
    #x = find_plus_positions(flood)
    #x.insert(0, [line_1, position_1])
    #nice_print(x)
    return matrix

def main():
    matrix = move(load_map())
    #print(flood)


if __name__ == "__main__":
    main()
