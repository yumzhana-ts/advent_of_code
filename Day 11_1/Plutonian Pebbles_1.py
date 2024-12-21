from utils import *
from model import *

def blinks(stones):
    stones_list = []
    for stone in stones:
        s = blink(stone)
        if isinstance(s, tuple): 
            stones_list.extend(s) 
        else:
            stones_list.append(s)
    return stones_list

def blink_loop(stones, length=75):
    if length == 0:
        return stones
    print(f"Iteration {75 - length}")
    return blink_loop(blinks(stones), length - 1)


def blink_loop(stones, length=75):
    if length == 0:
        return stones
    print(f"Iteration {75 - length}")
    return blink_loop(blinks(stones), length - 1)

def main():
    data = load_json("Day 11/big_data.json")
    stones = []
    
    for item in data:
        stones.append(Stone(item))
    test = blink_loop(stones)
    print(len(test))
    

if __name__ == "__main__":
    main()

