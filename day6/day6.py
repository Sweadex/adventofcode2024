from typing import Tuple

le = [
    ['.','.','.','.','#','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','#'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','#','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','#','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','#','.','.','^','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','#','.'],
    ['#','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','#','.','.','.']
]

def extract_list_from_file(file_path: str) -> Tuple[list[list[int]], list[list[int]]]:
    list = []
 

    with open(file_path) as f:
        for line in f:
            liste_tmp = []
            for val in line:
                if val != '\n':
                    liste_tmp.append(val)
            list.append(liste_tmp)

    return list

def get_guard_pos(map: list[list[chr]]) -> Tuple[int, int]:
    for y, y_line in enumerate(map):
        if '^' in y_line:
            return y, y_line.index('^')
        if '>' in y_line:
            return y, y_line.index('>')
        if 'v' in y_line:
            return y, y_line.index('v')
        if '<' in y_line:
            return y, y_line.index('<')
    return (-1,-1)

def is_out(y: int, x: int, map: list[list[chr]]):
    return (y >= len(map) or x >= len(map[0]) or x < 0 or y < 0)

def move_guard(guard_pos: Tuple[int, int], map: list[list[chr]]) -> Tuple[list[list[chr]], Tuple[int, int]]:
    init_y, init_x = guard_pos
    next_y, next_x = guard_pos

    if(map[init_y][init_x] == '^'):
        #print("up")
        next_y -= 1
    elif(map[init_y][init_x] == '>'):
        #print("right")
        next_x += 1
    elif(map[init_y][init_x] == 'v'):
        #print("down")
        next_y += 1
    elif(map[init_y][init_x] == '<'):
        #print("left")
        next_x -= 1
        
    if is_out(next_y, next_x, map):
        map[init_y][init_x] = 'X'
        return (map, (-1, -1))
    
    if (map[next_y][next_x] == '#'):
        #print("facing wall", map[init_y][init_x])
        if(map[init_y][init_x] == '^'):
            #print("rotate on right")
            map[init_y][init_x] = '>'
        elif(map[init_y][init_x] == '>'):
            #print("rotate on down")
            map[init_y][init_x] = 'v'
        elif(map[init_y][init_x] == 'v'):
            #print("rotate on left")
            map[init_y][init_x] = '<'
        elif(map[init_y][init_x] == '<'):
            #print("rotate on up")
            map[init_y][init_x] = '^'
        return move_guard(guard_pos, map)

    map[next_y][next_x] = map[init_y][init_x]
    map[init_y][init_x] = 'X'
    
    return (map, (next_y, next_x))

def get_number_of_explored_case(map: list[list[chr]]) -> int:
    pos = get_guard_pos(map)
    while True:
        if pos[0] >= 0 and pos[1] >= 0:
            map, pos = move_guard(pos, map)
        else:
            break

    sum_of_x = 0
    for line in map:
        sum_of_x += line.count("X")
        #print(line)
    return sum_of_x

#print("sum of x:", get_number_of_explored_case(le))

map_extract = extract_list_from_file("input_day6.csv")
print("sum of x:", get_number_of_explored_case(map_extract))