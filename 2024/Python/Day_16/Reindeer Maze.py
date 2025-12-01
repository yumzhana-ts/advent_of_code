from heapq import heappop, heappush
from utils import *
from helpers import *


def dijkstra(grid, start, end):
    queue = [(0, start, None, "R")]  # (cost, (x, y), previous_direction, direction)
    visited = set()

    while queue:
        current_cost, (x, y), prev_dir, current_dir = heappop(queue)
        if (x, y) == end:
            return current_cost

        if (x, y, prev_dir, current_dir) in visited:
            continue
        visited.add((x, y, prev_dir, current_dir))

        for direction, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy

            if check_range(nx, ny, grid):
                if current_dir is None or current_dir != direction:
                    rotation_cost = ROTATION_COST
                else:
                    rotation_cost = 0

                next_cost = current_cost + 1 + rotation_cost
                heappush(queue, (next_cost, (nx, ny), current_dir, direction))
    return -1

def main():
    data = load_json("Day_16/mini_data.json")
    grid = [list(row) for row in data]

    start = end = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start = (x, y)
            elif grid[y][x] == 'E':
                end = (x, y)

    shortest_path_cost = dijkstra(grid, start, end)
    print(f"Shortest path cost: {shortest_path_cost}")

if __name__ == "__main__":
    main()
