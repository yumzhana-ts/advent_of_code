import json
from itertools import product

def load_json(data):
    with open(data, "r") as file:
        return json.load(file)

def perform_operation(a, b, operation):
    operations = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "||": lambda x, y: int(str(x) + str(y)),
    }
    return operations.get(operation, lambda x, y: None)(a, b)

def process_numbers(item):
    result = item[0]
    item.pop(0)
    return result, item

def produce(item):
    all_combinations = list(product(['+', '*', '||'], repeat=len(item) - 1))
    return all_combinations

def calculate(operation, numbers):
    number = numbers[0]
    i = 1
    o = 0
    while i < len(numbers):
        number = perform_operation(number, numbers[i], operation[o])
        i+=1
        o+=1
    return(number)

def all_calculate(numbers, result):
    operations = produce(numbers)
    for operation in operations:
        total = calculate(operation, numbers)
        #print(total)
        if total == result:
            return result
    return(0)

def main():
    filename = "Day 7/big_data.json"
    data = load_json(filename)
    total = 0
    for i in range (len(data)):
        result, numbers = process_numbers(data[i])
        total += all_calculate(numbers, result)
    print(total)

if __name__ == "__main__":
    main()