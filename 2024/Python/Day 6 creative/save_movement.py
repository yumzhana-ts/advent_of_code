from move_helper import replace_step
from json_save import crazy_mind_down, crazy_mind_left, crazy_mind_right,crazy_mind_up


def handle_movement_up(matrix, line, position, wall, i):
    while True:
        if line <= 0:
            wall = True
            break
        elif matrix[line-1][0][position] != "#" and matrix[line-1][0][position] != ".":
            crazy_mind_up(matrix, i, line, position)
            i+=1
            matrix = replace_step(matrix, line, position, "X")
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
            matrix = replace_step(matrix, line, position, "X")
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
            matrix = replace_step(matrix, line, position, "X")
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
            matrix = replace_step(matrix, line, position, "X")
            matrix = replace_step(matrix, line, position-1, "<")
            position -= 1
        elif position == 0 or matrix[line][0][position-1] == "#":
            matrix = replace_step(matrix, line, position, "^")
            break
    return matrix, line, position, wall, i