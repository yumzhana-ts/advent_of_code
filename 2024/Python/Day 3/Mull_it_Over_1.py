

def syntax_check(text):
    result = 0
    for i in range(len(text)):
        instruction = text[i:]
        if instruction.startswith("mul(") :
            end_idx = instruction.index(")")
            instruction = instruction[4:end_idx]
            print(instruction)
            list = instruction.split(",")
            if len(list) == 2 and list[0].isdigit() and list[1].isdigit() and len(list[0]) <= 3 and len(list[1]) <=3 :
                result += int(list[0]) * int(list[1])
                print(list[0], "*", list[1],"= ", result)
    return result

def process_memory():
    with open("Day 3/memory.txt", "r") as file:
        text = file.read()
    #print(text)
	
    #text = "mul(2,)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(6,9878)"
    print(syntax_check(text))


process_memory()