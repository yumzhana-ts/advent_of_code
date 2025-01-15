DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

ROTATION_COST = 1000

def check_range(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != "#"

