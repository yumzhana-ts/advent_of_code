DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

def check_range(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def unlock_cheat(grid, wall):
    grid[wall[1]][wall[0]] = '.'
    return grid 

def lock_cheat(grid, wall):
    grid[wall[0]][wall[1]] = '#'
    return grid 