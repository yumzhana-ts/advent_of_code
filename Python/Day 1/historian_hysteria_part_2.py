import json

def indexed_list(i, list):
    c = []
    while i < len(list):
        c.append(list[i])
        i += 2
    return c

def appearence(n, list):
    l = []
    for item in list:
        if item == n:
            l.append(item)
    return len(l)

def similarity_score(l1, l2):
    i = 0
    score = 0
    while i < len(l1):
        score += l1[i] * appearence(l1[i], l2)
        i+=1
    return score


def list_process():
    with open("Day 1/list.json", 'r') as file:
        list = json.load(file)
    l1 = indexed_list(0, list)
    l2 = indexed_list(1, list)
    print(similarity_score(l1,l2))

list_process()