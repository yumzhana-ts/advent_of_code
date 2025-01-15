from utils import *
from model import *

def find_start(list):
    for i in range(len(list)):
        for n in range(len(list[i])):
            if list[i][n] != ['.']:
                return Plant(list[i][n][0], i, n)
            else:
                None

def refresh(list, plants):
    list = visualize(list, plants)
    #nice_print(list,"")
    #print("----------------------------------")
    start = find_start(list)
    return start

def visualize(list, plants):
    for plant in plants:
        list[plant.y][plant.x] = ['.']
    return(list)