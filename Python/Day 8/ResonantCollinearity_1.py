import json
from utils import nice_print, load_json
from itertools import combinations


def convert_to_list(data):
    list = [item for item in range(len())]
    
def get_line(data,line):
    return (data[line][0])

def get_case(data,line,position):
    return (data[line][0][position])

def set_position(data,line,position,insert):
    matrix = [item for item in data]
    matrix[line][0] = matrix[line][0][:position] + \
        insert + matrix[line][0][position + 1:]
    return (matrix)

def save_all_antennes(data):
    antenna_list = []
    for i in range (len(data)):
        for case in data[i][0]:
            if case != '.':
                antenna_list.append([case, i, data[i][0].index(case)])
    return(antenna_list)

def produce(set):
    all_pairs = list(combinations(set, 2))
    return all_pairs

def process_antennas(data):
    result = {}
    for item in data:
        key = item[0]
        value = item[1:]
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result 


def process_comb(comb):
    antinodes = []
    for group in comb:
        print("Group:")
        for pair in group:
            print(f"  Pair: {pair[0]} and {pair[1]}")
            difference_line = abs(pair[1][0] - pair[0][0])
            difference_position = abs(pair[1][1] - pair[0][1])
            if (pair[0][1] > pair[1][1]):
                first_aninode = [pair[0][0] - difference_line, pair[0][1] + difference_position]
                second_antinode = [pair[1][0] + difference_line, pair[1][1] - difference_position]
            else:
                first_aninode = [pair[0][0] - difference_line, pair[0][1] - difference_position]
                second_antinode = [pair[1][0] + difference_line, pair[1][1] + difference_position]
            antinodes.append(first_aninode)
            antinodes.append(second_antinode)
    return(antinodes)

def ran(matrix):
    return(len(matrix[0][0]),len(matrix))

def sort_antinodes(antinodes, data):
    max_case, max_line = ran(data)
    new = []
    nots = 0
    for i in range(len(antinodes)):
        line = antinodes[i][0]
        position = antinodes[i][1]
        
        # Ensure the line and position are within bounds
        if 0 <= line < max_line and 0 <= position < max_case:
            new.append([line, position])
    return new

def nice_print_comb(comb):
    for group in comb:
        print("Group:")
        for pair in group:
            print(f"  Pair: {pair[0]} and {pair[1]}")
            print()
        print()

def check_antinodes(data, list):
    matrix = data
    for i in range(len(list)):
        matrix = set_position(matrix,list[i][0],list[i][1],"#")
    nice_print(matrix)
    
def main():
    data = load_json("Day 8/big_data.json")
    print(ran(data))
    an = save_all_antennes(data)
    ab_dict = process_antennas(an)
    combinations = []
    for values in ab_dict.values():
        combinations.append(produce(values))
    anti = process_comb(combinations)
    print(anti)
    sort_anti = sort_antinodes(anti, data)
    print(sort_anti)
    check_antinodes(data, sort_anti)
    all_points = ab_dict.values()
    final = []
    for item in sort_anti:
        if item not in final:
            final.append(item)
    print(len(final))
    last_check = 0
    for item in data:
        for case in item[0]:
            if case == "#":
                last_check +=1
    print(last_check)
    
if __name__ == "__main__":
    main()