import json

def if_safe(list):
    is_descending = all(list[i] > list[i + 1] and list[i] - list[i + 1] <= 3 for i in range(len(list) - 1))
    is_ascending = all(list[i] < list[i + 1] and list[i + 1] - list[i] <= 3 for i in range(len(list) - 1))
    is_valid_sequence = is_descending or is_ascending
    return(is_valid_sequence)
    
def if_tolerate(list):
    for i in range(len(list)):
        new_list = list[:i] + list[i+1:]
        if if_safe(new_list) == True:
            return True
        
def process_report():
    with open("Day 2/report.json", "r") as file:
        list = json.load(file)
        safe_list = []
        for item in list:
            if if_safe(item) == True:
                safe_list.append(item)
                print(item)
            else:
                if if_tolerate(item) == True:
                    safe_list.append(item)
                    print(item)
    print(len(safe_list))
    
process_report()