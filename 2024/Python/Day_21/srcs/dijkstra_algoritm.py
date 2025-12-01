from heapq import heappop, heappush
from utils import *
from helpers import *
from collections import defaultdict

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
    queue = [(0, start, None)]
    parents = defaultdict(list)
    visited = {}
    min_cost = float("inf")
    all_end_states = []
    while queue:
        current_cost, (x, y), current_dir = heappop(queue)
        if current_cost > min_cost:
            continue
        if (x, y) in visited and visited[(x, y)] < current_cost:
            continue
        visited[(x, y)] = current_cost
        if current_dir is not None:
            parents[(x, y)].append(((x - DIRECTIONS[current_dir][0], y - DIRECTIONS[current_dir][1]), current_dir))
        if (x, y) == end:
            if current_cost < min_cost:
                min_cost = current_cost
                all_end_states = [(x, y)]
            elif current_cost == min_cost:
                all_end_states.append((x, y))
            continue
        explore_neighbors(queue, x, y, current_cost, grid, parents, visited)
    all_paths = []
    for end_state in all_end_states:
        generate_paths(parents, end_state, start, [], all_paths)
    return all_paths, min_cost

def generate_paths(parents, current, start, path, all_paths):
    if current == start:
        all_paths.append(path[::-1])
        return
    if current not in parents:
        return
    for prev, direction in parents[current]:
        generate_paths(parents, prev, start, path + [direction], all_paths)

def explore_neighbors(queue, x, y, current_cost, grid, parents, visited):
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = x + dx, y + dy
        if check_range(nx, ny, grid) and grid[ny][nx] != "#":
            new_cost = current_cost + 1
            if (nx, ny) not in visited or visited[(nx, ny)] > new_cost:
                heappush(queue, (new_cost, (nx, ny), direction))

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
