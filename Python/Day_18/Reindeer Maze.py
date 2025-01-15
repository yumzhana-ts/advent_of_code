from heapq import heappop, heappush
from utils import *
from helpers import *


def dijkstra(grid, start, end):
    queue = [(0, start)]  # (cost, (x, y))
    visited = set()
    #print(f"Starting Dijkstra's algorithm from {start} to {end}")
    while queue:
        current_cost, (x, y) = heappop(queue)
        #print(f"Visiting: ({x}, {y}), Cost: {current_cost}")
        if (x, y) == end:
            #print(f"Reached end at: ({x}, {y}) with cost: {current_cost}")
            return current_cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        #print(f"Visited set updated: {visited}")
        for direction, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy
            if check_range(nx, ny, grid):
                heappush(queue, (current_cost + 1, (nx, ny)))
                #print(f"Enqueued: ({nx}, {ny}), New Cost: {current_cost + 1}, Direction: {direction}")
    return -1




def main():
    start = (0, 0)
    end = (70, 70)
    i = 1024
    while i < 3450:
        data = load_json(f"Day_18/maps/grid_{i}.json")
        print(f"processing grid_{i}")
        grid = [list(row) for row in data]
        print(grid)
        shortest_path_cost = dijkstra(grid, start, end)
        if shortest_path_cost == -1:
            break
        i+=1
        #print(f"Shortest path cost: {shortest_path_cost}")
        

if __name__ == "__main__":
    main()
