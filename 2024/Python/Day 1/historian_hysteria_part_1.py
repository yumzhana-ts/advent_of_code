import json

def indexed_list(i, list):
    c = []
    while i < len(list):
        c.append(list[i])
        i += 2
    return c

def find_smallest(list):
    i = 0
    min = list[i]
    while i < len(list):
        if list[i] < min:
            min = list[i]
        i+=1
    return min

def compare(l1, l2):
    i = 0
    sum = 0
    while i < 1000: 
        #print("index",i,":", find_smallest(l1), "-", find_smallest(l2))
        if find_smallest(l1) > find_smallest(l2):
            sum += find_smallest(l1) - find_smallest(l2)
        else:
            sum += find_smallest(l2) - find_smallest(l1)
        #print("sum:", sum)
        l1.pop(l1.index(find_smallest(l1)))
        l2.pop(l2.index(find_smallest(l2)))
        i+=1
    return sum

def compare(l1, l2):
    i = 0
    sum = 0
    while i < 1000: 
        #print("index",i,":", find_smallest(l1), "-", find_smallest(l2))
        if find_smallest(l1) > find_smallest(l2):
            sum += find_smallest(l1) - find_smallest(l2)
        else:
            sum += find_smallest(l2) - find_smallest(l1)
        #print("sum:", sum)
        l1.pop(l1.index(find_smallest(l1)))
        l2.pop(l2.index(find_smallest(l2)))
        i+=1
    return sum

def list_process():
    with open("Day 1/list.json", 'r') as file:
        list = json.load(file)
    l1 = indexed_list(0, list)
    l2 = indexed_list(1, list)
    print("total sum:", compare(l1, l2))
    


list_process()