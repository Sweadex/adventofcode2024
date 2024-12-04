from typing import Tuple, List

l_e = [
    ["M","M","M","S","X","X","M","A","S","M"],
    ["M","S","A","M","X","M","S","M","S","A"],
    ["A","M","X","S","X","M","A","A","M","M"],
    ["M","S","A","M","A","S","M","S","M","X"],
    ["X","M","A","S","A","M","X","A","M","M"],
    ["X","X","A","M","M","X","X","A","M","A"],
    ["S","M","S","M","S","A","S","X","S","S"],
    ["S","A","X","A","M","A","S","A","A","A"],
    ["M","A","M","M","M","X","M","M","M","M"],
    ["M","X","M","X","A","X","M","A","S","X"]
]

directionnals_pairs =[
    # y,x
    [0,1],
    [1,1],
    [1,0],
    [1,-1],
    [0,-1],
    [-1,-1],
    [-1,0],
    [-1,1]
]

def extract_list_from_file(file_path: str) -> list[list[int]]:
    liste = []
    
    with open(file_path) as f:
        for line in f:
            liste_tmp = []
            for char in line:
                liste_tmp.append(char)
            liste.append(liste_tmp)
    
    return liste

def count_key(list: list[list[int]], y_index: int, x_index: int, key: str) -> int:
    count = 0
    for direction in directionnals_pairs:
        if(y_index + ((len(key) - 1) * direction[0]) < 0):
            continue
        if(x_index + ((len(key) - 1) * direction[1]) < 0):
            continue
        for i, char in enumerate(key):
            try:
                if(list[y_index + ((i) * direction[0])][x_index + ((i) * direction[1])] != char):
                    break
            except Exception as e:
                break
            if (i == len(key) - 1):
                count += 1
    return count

def count_key_in_list(list: list[list[int]], key: str) -> int:
    count = 0
    for y, line in enumerate(list):
        for x, char in enumerate(line):
            if char == key[0]:
                count_to_add = count_key(list, y, x, key)
                count += count_to_add
    return count

def is_x_mas(list: list[list[int]], y_index: int, x_index: int) -> bool:
    count = 0
    for y in [-1,1]:
        if(y_index + y) < 0:
            continue
        for x in [-1,1]:
            if(x_index + x) < 0:
                continue
            try:
                if(list[y_index+y][x_index+x] == 'M' and list[y_index-y][x_index-x] == 'S'):
                    count += 1
                if count == 2:
                    return True
            except Exception:
                continue
    return False

def count_x_mas_in_list(list: list[list[int]]) -> int:
    count = 0
    for y, line in enumerate(list):
        for x, char in enumerate(line):
            if char == 'A' and is_x_mas(list, y, x):
                count += 1
    return count
    
#print(count_key(l_e,9,3,"XMAS"))

#print(count_key_in_list(extract_list_from_file("input_day4.csv"), "XMAS"))

print(count_x_mas_in_list(l_e))

print(count_x_mas_in_list(extract_list_from_file("input_day4.csv")))