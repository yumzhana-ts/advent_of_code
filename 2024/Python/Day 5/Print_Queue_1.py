import json

def process_rules():
    with open("Day 5/big_rules.json", "r") as file:
        list = json.load(file)
    return list
    
def process_numbers():
    with open("Day 5/big_numbers.json", "r") as file:
        list = json.load(file)
    check = []
    for item in list:
        if_all = []
        for i in range(len(item) - 1):
            fl = False
            l = []
            l.append(item[i])
            l.append(item[i+1])
            for ia in process_rules():
                if ia == l:
                    fl = True
                    if_all.append(fl)
        if(len(item) - 1) == len(if_all):
            check.append(item)
    return(check)

    
def process_all():
    result = 0
    for item in process_numbers():
        i = int(len(item) / 2)
        result = result + item[i]
    print(result)
process_all()

