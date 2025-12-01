from heapq import heappop, heappush
from utils import *
from helpers import *

def shortest_path_algorithm(grid):
    start, end = start_end(grid)
    list = []
    i = 0
    total = len(grid)
    paths = []
    
    mini_n = total * total
    big_n = 10510
    print("Starting shortest path computation...")
    while i < mini_n:
        shortest_path_cost = dijkstra(grid, start, end, list)
        print(f"Processing task {i}")
        if shortest_path_cost != 9380:
            paths.append(shortest_path_cost)
        i += 1

    print("Saving output to 'paths_output.json'...")
    with open("Day_20/data/output.json", "w") as f:
        json.dump(paths, f)

    print("Computation completed and output saved.")
    print(paths)
    return paths

def start_end(grid):
    start = end = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start = (x, y)
            elif grid[y][x] == 'E':
                end = (x, y)
    return start, end

def explore_neighbors(queue, x, y, current_cost, grid, visited, used, finish):
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = x + dx, y + dy
        if check_range(nx, ny, grid):
            if grid[ny][nx] != "#":
                heappush(queue, (current_cost + 1, (nx, ny)))
                if finish == 20:
                    used = True
                if finish > 0 and used is False:
                    finish += 1
            elif grid[ny][nx] == "#" and finish == 0 and [ny, nx] not in visited and used is False:
                if finish == 20:
                    used = True
                start = [ny, nx]
                visited.append(start)
                heappush(queue, (current_cost + 1, (nx, ny)))
                finish += 1
            elif grid[ny][nx] == "#" and finish > 0 and finish <= 20 and used is False:
                heappush(queue, (current_cost + 1, (nx, ny)))
                if finish == 20:
                    used = True
                finish += 1
    return visited, used, finish

def dijkstra(grid, start, end, list):
    queue = [(0, start)]  # (cost, (x, y))
    visited = set()
    used = False
    finish = 0
    while queue:
        current_cost, (x, y) = heappop(queue)
        if (x, y) == end:
            return current_cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        list, used, finish = explore_neighbors(queue, x, y, current_cost, grid, list, used, finish)
    return -1
