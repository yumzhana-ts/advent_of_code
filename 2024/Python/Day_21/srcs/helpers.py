DIRECTIONS = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

def check_range(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def process_multiple(list1, list2):
    big_list = []
    for items in list1:
        for i in list2:
            big_list.append(items + i)
    return big_list

def process_list(chunks):
    start = chunks[0]
    d = 1
    while d < len(chunks):
        big_list = process_multiple(start, chunks[d])
        start = big_list
        d+=1
    return big_list