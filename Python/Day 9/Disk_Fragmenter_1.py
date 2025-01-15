from utils import load_json, nice_print

    
def add_case(list,position, case):
    list[position] = case
    return list

    
def nice_print(list):
    result = "".join("".join(item) for item in list)
    return result

def fix_data(data):
    if len(data[0]) % 2 != 0:
        data[0] = data[0][:len(data[0])] + "0"
    return data

def process_dict():
    filename = "Day 9/big_data.json"
    data = fix_data(load_json(filename)) 
    dict = process_data(data[0])
    return (dict)

def process_data(data):
    dicts = {}
    n = 0
    i = 0
    while i < len(data) - 1:
        file = data[i]
        space = data[i + 1]
        key = f"{n}"
        dicts[key] = [file, space]
        n += 1
        i += 2
    return dicts

def print_disk_map(disk_map):
    list = []
    for key, value in disk_map.items():
        list.extend([key] for _ in range(int(value[0])))
        list.extend(['.'] for _ in range(int(value[1])))
    return(list)

def swap_cases(list):
    i = 0
    while True:
        try:
            index = list.index(['.'])
        except ValueError:
            index = -1
        if index == -1:
            break
        list = add_case(list, index, list[len(list) - 1])
        list = list[:-1]
        i+=1
    return list

def count(list):
    i = 0
    result = 0
    n = 0
    for i in range(len(list)):
        result += n * int(list[i][0])
        #print(i, " * ", int(list[i][0]))
        n+=1
    return result

def main():
    dict = process_dict()
    list = print_disk_map(dict)
    list = swap_cases(list)
    #print(list)
    print(count(list))

if __name__ == "__main__":
    main()