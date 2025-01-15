from itertools import product
from concurrent.futures import ProcessPoolExecutor
import json
import logging

logging.basicConfig(level=logging.INFO)

def product_of_strings(strings, target):
    max_length = len(target)
    for length in range(1, max_length + 1):
        for combination in product(strings, repeat=length):
            combined_string = "".join(combination)
            if combined_string == target:
                return True
    return False

def process_combination(big_towel, item):
    result = product_of_strings(big_towel, item[0])
    logging.debug(f"Processed combination: {item[0]} -> {'Match' if result else 'No Match'}")
    return result

def main():
    #big_towel = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    big_towel = load_json("Day_19/big_data_1.json")
    combinations = load_json("Day_19/big_data.json")
    #combinations = load_json("Day_19/mini_data.json")
    count = 0
    
    logging.info("Starting parallel processing...")
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_combination, [big_towel] * len(combinations), combinations))
        
    count = sum(results)
    logging.info(f"Total matches found: {count}")

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    main()



def product_of_strings(strings, target):
    max_length = len(target)
    print(f"Target: {target}, Max Length: {max_length}")
    for length in range(1, max_length + 1):
        for combination in product(strings, repeat=length):
            combined_string = "".join(combination)
            if combined_string == target:
                print(f"Match found: {combined_string}")
                return True
    print("No match found.")
    return False
    

def main():
    towel = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    big_towel = load_json("Day_19/big_data_1.json")
    combinations = load_json("Day_19/big_data.json")
    count = 0
    for item in combinations:
        if product_of_strings(big_towel, item[0]) == True:
            count+=1
    print(count)