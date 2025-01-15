from utils import *
from model import *

def find_start(list):
    for i in range(len(list)):
        for n in range(len(list[i])):
            if list[i][n] != ['.']:
                return Plant(list[i][n][0], i, n)
            else:
                None

def expand(matrix, border_value=['*']):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    expanded_matrix = []
    expanded_matrix.append([border_value] * (cols + 2))
    for row in matrix:
        expanded_matrix.append([border_value] + row + [border_value])
    expanded_matrix.append([border_value] * (cols + 2))
    return expanded_matrix

    
def visualize(list, plants):
    for plant in plants:
        list[plant.y][plant.x] = ['.']
    return(list)

def refresh(list, plants):
    list = visualize(list, plants)
    #nice_print(list,"")
    print("----------------------------------")
    start = find_start(list)
    return start

def border_refresh(list, plants, borders):
    list = visualize(list, plants)
    crazy = expand(list)
    print("______________")
    for border in borders:
        crazy[border.y+1][border.x+1] = ['#']
    nice_print(crazy, "")
    row = 0
    for item in crazy:
        i = 0
        for it in item:
            if it == ['#']:
                row+=1
            else:
                i+=1
    print(row)

def column(grid, plants):
    plant_type = [plants[0].get_type()]
    col_c = 0
    for col in range(len(grid[0])):
        i = 0
        while i < len(grid):
            if grid[i][col] == plant_type:
                col_c += 1
                current_type = grid[i][col]
                while i < len(grid) and grid[i][col] == current_type:
                    i += 1
            else:
                i += 1
    print(col_c)
    
def row(grid, plants):
    plant_type = [plants[0].get_type()]
    row_c = 0
    for row in grid:
        j = 0
        while j < len(row):
            if row[j] == plant_type:
                row_c += 1
                current_type = row[j]
                while j < len(row) and row[j] == current_type:
                    j += 1
            else:
                j += 1
    print(row_c)