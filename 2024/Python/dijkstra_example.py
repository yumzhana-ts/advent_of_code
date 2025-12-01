from heapq import heappop, heappush
from utils import *
from helpers import *

def shortest_path_algorithm(grid, start_case, end_case):
    start, end = start_end(grid, start_case, end_case)
    shortest_path_cost = dijkstra(grid, start, end)
    return shortest_path_cost

def start_end(grid, start_case, end_case):
    start = end = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == start_case:
                start = (x, y)
            elif grid[y][x] == end_case:
                end = (x, y)
    return start, end

def explore_neighbors(queue, x, y, current_cost, grid, parent, visited):
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = x + dx, y + dy
        if check_range(nx, ny, grid) and (nx, ny) not in visited:
            if grid[ny][nx] != ".":
                new_cost = current_cost + 1
                heappush(queue, (new_cost, (nx, ny), direction))
    return parent

def dijkstra(grid, start, end):
    queue = [(0, start, None)]  # (cost, (x, y), direction)
    parent = {}
    visited = {}
    paths = []
    min_cost = float("inf")
    
    while queue:
        current_cost, (x, y), current_dir = heappop(queue)
        
        # Stop processing if this node is worse than the minimum cost
        if current_cost > min_cost:
            continue
        
        if (x, y) in visited and visited[(x, y)] <= current_cost:
            continue
        
        visited[(x, y)] = current_cost
        
        # Update parent only if this is the first time reaching the node
        if current_dir is not None:
            parent[(x, y)] = ((x - DIRECTIONS[current_dir][0], y - DIRECTIONS[current_dir][1]), current_dir)
        
        # If end node is reached, collect the path
        if (x, y) == end:
            if current_cost < min_cost:
                min_cost = current_cost
                paths = [traverse_route(parent, end, start)]
            elif current_cost == min_cost:
                paths.append(traverse_route(parent, end, start))
            continue
        
        explore_neighbors(queue, x, y, current_cost, grid, parent, visited)
    
    return paths, min_cost

def traverse_route(parent, end, start):
    path_with_directions = []
    directions = []
    current = end
    while current != start:
        if current not in parent:
            return []  # Return an empty path if no valid path exists
        previous, direction = parent[current]
        directions.append(direction)
        current = previous
    directions.reverse()
    return directions
