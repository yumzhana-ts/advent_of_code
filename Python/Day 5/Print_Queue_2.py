import json

def load_rules():
    with open("Day 5/big_rules.json", "r") as file:
        return json.load(file)

def load_numbers():
    with open("Day 5/big_numbers.json", "r") as file:
        return json.load(file)

def is_valid_order(pair, rules):
    return pair in rules

def is_sorted(item, rules):
    return all(is_valid_order([item[i], item[i + 1]], rules) for i in range(len(item) - 1))
    
def process_list(numbers, rules):
    numbers = [item for item in numbers if not is_sorted(item, rules)]
    return numbers

def process_swap(numbers, rules):
    numbers = process_list(numbers, rules)
    for item in numbers:
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(item) - 1):
                if not is_valid_order([item[i], item[i+1]], rules):
                    item[i], item[i+1] = item[i+1], item[i]
                    swapped = True
    return numbers

def main():
    rules = load_rules()
    numbers = load_numbers()
    sorted_numbers = process_swap(numbers, rules)
    result = 0
    for item in sorted_numbers:
        i = int(len(item) / 2)
        result = result + item[i]
    print(result)

if __name__ == "__main__":
    main()


        elif file[line][0][position] == '>':
            if file[line][0][position+1] == ".":
                matrix = replace_step(file, line, position, "X")
                matrix = replace_step(file, line, position+1, ">")
                position+=1
                if matrix[line][0][position] != ".":
                    wall = True