from model import *
from utils import *
from getters import *

def starting_points(data):
    nodes = []
    i = 0
    for d in range(len(data)):
        for i in range(len(data[d])):
            if data[d][i] == ['0']:
                node = Node(i, d, data[d][i])
                nodes.append(node)
    return nodes

def move(data, parent_node):
    right_child = get_right(parent_node, data)
    left_child = get_left(parent_node, data)
    up_child = get_up(parent_node, data)
    down_child = get_down(parent_node, data)

    children = [right_child, left_child, up_child, down_child]
    valid_children = [child for child in children if child is not None]
    return valid_children

def add_children(data, nodes):
    for node in nodes:
        valid_children = move(data, node)
        for child_node in valid_children:
            node.set_child(child_node)
    return nodes


def add_children_recursive(data, nodes, depth=1):
    for node in nodes:
        valid_children = move(data, node) 
        for child_node in valid_children:
            node.set_child(child_node)
        if node.children:
            add_children_recursive(data, node.children, depth=depth + 1)


def print_nodes_with_children(nodes, depth=0, counter=None):
    if counter is None:
        counter = {'count': 0}
    for node in nodes:
        if node.case == '9':
            counter['count'] += 1
        if node.children:
            print_nodes_with_children(node.children, depth + 2, counter)
    return counter['count']


def main():
    data = string_to_list(load_json('Day 10_1/big_data.json'))
    nodes = starting_points(data)
    starting_nodes = starting_points(data)
    add_children_recursive(data, starting_nodes)
    print(print_nodes_with_children(starting_nodes))
        
if __name__ == "__main__":
    main()
