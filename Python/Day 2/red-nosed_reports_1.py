import json

def if_increase(list):
    i = 0
    while i < len(list):
        result = list[i] - list[i+1]
        if (result > 0):
            return 1
        if (result < 0):
            return 0
        if (result == 0):
            i+=1

def if_safe(list):
    i = 1
    number = list[0]
    safe = 1
    increase = if_increase(list)
    while i < len(list):
        if increase == 1:
            result = number - list[i]
            print("difference of ", number, " and ", list[i], ":", result)
            if result <= 0 or result > 3:
                safe = 0
                break
        else:
            result = list[i] - number
            print("difference of ", number, " and ", list[i], ":", result)
            if result <= 0 or result > 3:
                safe = 0
                break
        number = list[i]
        i+=1
    print("state is", safe)
    return safe
    

def process_report():
    with open("Day 2/report.json", "r") as file:
        list = json.load(file)
        safe_list = []
        for item in list:
            if if_safe(item) == 1:
                print(item)
                safe_list.append(item)
    print(len(safe_list))
    
process_report()