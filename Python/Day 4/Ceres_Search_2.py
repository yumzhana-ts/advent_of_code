import json

def process_list():
    total = 0
    with open("Day 4/big_search.json", "r") as file:
        list = json.load(file)
    d = 0
    l = []
    while d < (len(list) - 2):
        i = 0
        while i < len(list[d]):
            if(len(list[d][i:i+3]) == 3 and len(list[d+1][i:i+3]) == 3 and len(list[d+1][i:i+3]) == 3):
                if list[d][i:i+3].startswith("M") and list[d][i:i+3].endswith("S") and list[d+2][i:i+3].startswith("M") and list[d+2][i:i+3].endswith("S"):
                    if list[d+1][i+1:].startswith("A"):
                        l.append("banana")
                elif list[d][i:i+3].startswith("S") and list[d][i:i+3].endswith("M") and list[d+2][i:i+3].startswith("S") and list[d+2][i:i+3].endswith("M"):
                    if list[d+1][i+1:].startswith("A"):
                        l.append("banana")
                elif list[d][i:i+3].startswith("M") and list[d][i:i+3].endswith("M") and list[d+2][i:i+3].startswith("S") and list[d+2][i:i+3].endswith("S"):
                    if list[d+1][i+1:].startswith("A"):
                        l.append("banana")
                elif list[d][i:i+3].startswith("S") and list[d][i:i+3].endswith("S") and list[d+2][i:i+3].startswith("M") and list[d+2][i:i+3].endswith("M"):
                    if list[d+1][i+1:].startswith("A"):
                        l.append("banana")
            i+=1
        d+=1
    print(len(l))

process_list()

