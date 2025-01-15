
def is_within_bounds(line, position, max = 50):
    return 0 <= line < max and 0 <= position < max

def multiply_left_up(antinodes, first_aninode, difference_line, difference_position):
    first_aninode = [first_aninode[0] - difference_line, first_aninode[1]  + difference_position]
    if is_within_bounds(first_aninode[0], first_aninode[1]) == True:
        antinodes.append(first_aninode)
        multiply_left_up(antinodes,first_aninode, difference_line, difference_position)
    else:
        return 

def multiply_left_down(antinodes, second_antinode, difference_line, difference_position):
    second_antinode = [second_antinode[0] + difference_line, second_antinode[1] - difference_position]
    if is_within_bounds(second_antinode[0], second_antinode[1]) == True:
        antinodes.append(second_antinode)
        multiply_left_down(antinodes,second_antinode, difference_line, difference_position)
    else:
        return 

def multiply_right_up(antinodes, first_aninode, difference_line, difference_position):
    first_aninode = [first_aninode[0] - difference_line, first_aninode[1]  - difference_position]
    if is_within_bounds(first_aninode[0], first_aninode[1]) == True:
        antinodes.append(first_aninode)
        multiply_right_up(antinodes,first_aninode, difference_line, difference_position)
    else:
        return 

def multiply_right_down(antinodes, second_antinode, difference_line, difference_position):
    second_antinode = [second_antinode[0] + difference_line, second_antinode[1] + difference_position]
    if is_within_bounds(second_antinode[0], second_antinode[1]) == True:
        antinodes.append(second_antinode)
        multiply_right_down(antinodes,second_antinode, difference_line, difference_position)
    else:
        return 

def check_left_up(first_aninode, difference_line, difference_position):
    if is_within_bounds(first_aninode[0], first_aninode[1]) == True:
        return(True)
    else: 
        return(False)
        
def check_left_down(second_antinode, difference_line, difference_position):
    if is_within_bounds(second_antinode[0], second_antinode[1]) == True:
        return(True)
    else:
        return False

def check_right_up(first_aninode, difference_line, difference_position):
    if is_within_bounds(first_aninode[0], first_aninode[1]) == True:
        return True
    else:
        return False

def check_right_down(second_antinode, difference_line, difference_position):
    if is_within_bounds(second_antinode[0], second_antinode[1]) == True:
        return True
    else:
        return False