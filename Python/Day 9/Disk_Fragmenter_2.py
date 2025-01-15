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

def save_dots(list):
    count = 0
    try:
        start_index = list.index(['.'])
    except ValueError:
        index = -1
    if start_index != -1:
        index = start_index
        while list[index][0] == '.':
            count += 1
            index += 1
        return [start_index,count]
    else:
        return None

def save_all_dots(list):
    i = 0
    dots = []
    while i < len(list):
        if list[i][0] == '.':
            count = 0
            d = i
            while d < len(list) and list[d][0] == '.':
                count += 1
                d+=1
            dots.append([i, count])
            i = d
        i+=1
    return dots

def save_all_chunks(lst):
    i = 0
    chunks = []
    while i < len(lst):
        if lst[i][0].isdigit():
            case = lst[i][0]
            count = 0
            d = i
            while d < len(lst) and lst[d][0] == case:
                count += 1
                d += 1
            chunks.append([case, count, i])
            i = d
        else:
            i += 1
    return chunks

def save_chunks(list):
    count = 0 
    chunks = []
    case = list[len(list)-1]
    i = len(list)-1
    while i > 0 and list[i] == case:
        i-=1
        count+=1
    return [case, count, i+1]

def add_chunks(list, case, position, occurence):
    i = 0
    while i < occurence:
        list[position+i] = [case]
        i+=1
    return(list)

def remove_chunks(list, index, occurence):
    i = 0
    while i < occurence:
        list[index] = ["*"]
        i+=1
        index+=1
    return list

def rearrange(list):
    dots = save_dots(list)
    print(dots)
    chunks = save_chunks(list)
    print(chunks)
    if dots[1] >= chunks[1]:
        #print("i am here")
        list = remove_chunks(list,chunks[2],chunks[1])
        #nice_print(list)
        list = add_chunks(list, chunks[0], dots[0], chunks[1])
    return(list)

def massive_rearrange(lst, chunks, dots):
    for chunk in chunks:
        dots = save_all_dots(lst)
        for dot in dots:
            if dot[1] >= chunk[1]:
                print(chunk, dot)
                if chunk[2] > dot[0]:
                    lst = remove_chunks(lst, chunk[2], chunk[1])
                    lst = add_chunks(lst, chunk[0], dot[0], chunk[1])
                    #print(nice_print(lst))
                    #print(dot, chunk)
                    break
    return(lst)

def count(list):
    i = 0
    result = 0
    n = 0
    for i in range(len(list)):
        if(list[i][0] == '.' or list[i][0] == '*'):
            n+=1
            continue
        else:
            result += n * int(list[i][0])
            #print(i, " * ", int(list[i][0]))
            n+=1
    return result

            
def main():
    dict = process_dict()
    list = print_disk_map(dict)
    #print(nice_print(list))
    #new = rearrange(list)
    #print(nice_print(new))
    dots = save_all_dots(list)
    chunks = save_all_chunks(list)
    chunks.reverse()
    print("doing change")
    list = massive_rearrange(list, chunks, dots)
    #print(list)
    print(count(list))
    #print(nice_print(list))
    #print(list)

if __name__ == "__main__":
    main()