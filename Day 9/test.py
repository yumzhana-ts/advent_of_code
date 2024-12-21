data = ["00992111777.44.333....5555.6666.....8888.."]

def test(data):
    result = 0
    i = 0
    for item in data[0]:
        if(item) == '.':
            i+=1
            continue
        else:
            result += int(item) * i
            i+=1
    print(result)
test(data)