from utils import *
from getters import *
from step_check import *

def process_single_parent(data, parent):
    print(f"{GREEN}- processing parent: {parent}")
    childs = move(data, parent)
    nice_list_print(childs, "child")
    return childs

def process_parent_list(data, parents):
    print(f"{GREEN}Processing list from parent points: {parents}{RESET}")
    all_childs = []
    for parent in parents:
        childs = process_single_parent(data, parent)
        for child in childs:
            if child not in all_childs:
                all_childs.append(child)
    return all_childs

def process_parent_list_multiple(data, start, iterations=9):
    current_parents = start
    for i in range(iterations):
        #print(f"Iteration {i + 1}:")
        current_parents = process_parent_list(data, current_parents)
    return current_parents
