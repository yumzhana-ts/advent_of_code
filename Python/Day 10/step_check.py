from getters import *

def starting_points(data):
    starts = []
    i = 0
    for d in range(len(data)):
        for i in range(len(data[d])):
            if data[d][i] == ['0']:
                starts.append([d,i])
    return starts

def move(data, parent, path):
    right_child = get_right(parent[0], parent[1], data)  
    left_child = get_left(parent[0], parent[1], data)
    up_child = get_up(parent[0], parent[1], data)
    down_child = get_down(parent[0], parent[1], data)
    children = [right_child, left_child, up_child, down_child]
    valid_children = [child for child in children if child is not None]
    return valid_children