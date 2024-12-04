import json

def horizontal_appearence(list):
    l = []
    for i in range(len(list)):
        search = list[i:]
        if search.startswith("XMAS") or search.startswith("SAMX"):
            l.append(search)
    return len(l)

def vertical_sort(list):
    l = []
    for i in range(len(list)):
        comb = ""
        for k in range(len(list)):
            a = list[k][i]
            comb = comb + a
        l.append(comb)
    return l

def diagonal(matrix, hor):
    diagonal = ''.join(str(matrix[i][i+hor]) for i in range(4))
    return diagonal

def reverse_diagonal(matrix, hor):
    diagonal = ''.join(str(matrix[i][len(matrix[i])-i-1-hor]) for i in range(4))
    return diagonal

def diagonal_list(list):
    length = len(list[0]) - 3
    l = []
    i = 0  # Initialize the counter for the while loop
    try:
        while i < length:  # Loop while i is less than length
            l.append(diagonal(list, i))  # Shift by d and get the diagonal
            l.append(reverse_diagonal(list, i))  # Shift by d and get the diagonal
            i += 1  # Increment i in the loop
        return l
    except IndexError:
        print("out of range")
        
def process_fucking_list(list):
    i = 0
    l =[]
    while len(list) >= 4:
        l += diagonal_list(list)
        list.pop(0)
        i+= 1
    return(l)


def process_search():
    total = 0
    with open("Day 4/big_search.json", "r") as file:
        list = json.load(file)
        #print(list)
    for item in list:
        total += horizontal_appearence(item)
    for item in vertical_sort(list):
        total += horizontal_appearence(item)
    for item in process_fucking_list(list):
        total += horizontal_appearence(item)
    print(total)

process_search()

