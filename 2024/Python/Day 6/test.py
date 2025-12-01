import json

def nice_print(matrix):
    for item in matrix:
        print(item)

def main():
    with open("Day 6/mini/map_33.json", "r") as file:
        list = json.load(file)
    nice_print(list)
    
if __name__ == "__main__":
    main()