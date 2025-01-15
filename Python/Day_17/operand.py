def combo(number, registers):
    if number >= 0 and number <= 3:
        return number
    elif number == 4:
        return registers[0]
    elif number == 5:
        return registers[1]
    elif number == 6:
        return registers[2]
    else:
        return None

def input(type, number, registers):
    if type == "combo":
        return combo(number, registers)
    elif type == "literal" and number >=0 and number <=7:
        return number
    else:
        return None

#def main():
#    registers = [729,0,0]
#    number = input("literal", 8, registers)
    

#if __name__  == "__main__":
#    main()