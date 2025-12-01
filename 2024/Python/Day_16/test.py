def create_grid(data):
    # Find the maximum x and y values to determine grid size
    max_x = 0
    max_y = 0
    
    for _, coords in data:
        for x, y in coords:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    
    # Create a grid initialized with '.' representing empty spaces
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Mark walls ('#') in the grid
    for _, coords in data:
        for x, y in coords:
            grid[y][x] = '#'
    
    # Mark start ('S') and end ('E') points
    grid[coords[0][1]][coords[0][0]] = 'S'
    grid[y][x] = 'E'

    return grid

# Example usage
data = [
(7036, [(1, 13), (1, 12), (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (12, 13), (13, 13), (13, 12), (13, 11), (13, 10), (13, 9), (13, 8), (13, 7), (13, 6), (13, 5), (13, 4), (13, 3), (13, 2), (13, 1)])
]
grid = create_grid(data)

# Output the grid
for row in grid:
    print(''.join(row))