import math
from utils import *
import multiprocessing
from multiprocessing import Pool, Manager, cpu_count
from operand import *

def get_instruction_pointer(pointer):
    data = [2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0]
    try:
        li = [data[i] for i in range(0, len(data), 2)]
        new_pointer = pointer
        new_data = data[new_pointer * 2:]
        return(new_data)
    except:
        raise IndexError

def instruction_pointer(data):
    data = data[2:]
    return data

#TODO: passed
def adv(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing adv...{RESET}")
    numerator = registers[0]
    exponential = input("combo", operand, registers)
    denominator = 2 ** exponential
    result = numerator / denominator
    registers[0] = int(result)
    data = instruction_pointer(data)
    return registers, data

#TODO: passed
def bxl(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing bxl...{RESET}")
    number = registers[1]
    result = number ^ input("literal", operand, registers)
    registers[1] = result
    data = instruction_pointer(data)
    return registers, data

#TODO: passed 
def bst(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing bst...{RESET}")
    number = input("combo", operand, registers)
    result = number % 8
    registers[1] = result
    data = instruction_pointer(data)
    return registers, data

#TODO: passed
def jnz(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing jnz...{RESET}")
    number = registers[0]
    if number == 0:
        data = instruction_pointer(data)
    else:
        data = get_instruction_pointer(input("literal", operand, registers))
    return registers, data

#TODO: passed
def bxc(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing bxc...{RESET}")
    num_1 = registers[1]
    num_2 = registers[2]
    result = num_1 ^ num_2
    registers[1] = result 
    data = instruction_pointer(data)
    return registers, data

#TODO: passed 
def out(registers, operand, data, print_list):
    #print(f"{GREEN}processing out...{RESET}")
    number = input("combo", operand, registers) 
    modulo = number % 8
    print_list.append(modulo)
    data = instruction_pointer(data)
    return registers, data

#TODO: should be ok
def bdv(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing bdv...{RESET}")
    numerator = registers[0]
    exponential = input("combo", operand, registers)
    denominator = 2 ** exponential
    result = numerator / denominator
    registers[1] = int(result)
    data = instruction_pointer(data)
    return registers, data

#TODO: should be ok
def cdv(registers, operand, data, print_list = None):
    #print(f"{GREEN}processing cdv...{RESET}")
    numerator = registers[0]
    exponential = input("combo", operand, registers)
    denominator = 2 ** exponential
    result = numerator / denominator
    registers[2] = int(result)
    data = instruction_pointer(data)
    return registers, data

cases = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

def process_data(registers):
    data = [2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0]
    print_list = []
    while True:
        operand = data[1]
        #print(f"Data: {data}")
        #print(f"Initial Registers: {registers}")
        #print(f"Operation: {data[0]}, Operand: {operand}")
        registers, data = cases.get(data[0])(registers, operand, data, print_list)
        if len(data) == 0:
            break
    return print_list

def process_data_chunk(start, end, stop_event):
    for i in range(start, end):
        if stop_event.is_set():
            break
        if process_data([i, 0, 0]) == [2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0]:
            stop_event.set()
            return i, start, end
    return None, start, end

# Helper function for multiprocessing
def process_wrapper(args):
    return process_data_chunk(*args)

def main():
    block_size = 100000
    range_limit = 1000000000000
    num_workers = cpu_count()

    with Manager() as manager:  # Use Manager for shared objects
        stop_event = manager.Event()

        with Pool(processes=num_workers) as pool:
            tasks = [(start, min(start + block_size, range_limit), stop_event)
                     for start in range(139100000, range_limit, block_size)]
            
            for result, start, end in pool.imap_unordered(process_wrapper, tasks):
                # Log the progress for each processed block
                print(f"Processed block: start={start}, end={end}")
                
                if result is not None:
                    print(f"Value found: {result}")
                    stop_event.set()
                    break

        if not stop_event.is_set():
            print("Value not found")

if __name__ == "__main__":
    main()