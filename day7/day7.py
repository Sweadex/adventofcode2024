from typing import Tuple

ADD_OPERATOR = 0
MULTIPLY_OPERATOR = 1

OPERATORS_TYPE = [ADD_OPERATOR, MULTIPLY_OPERATOR]

le = [
    (190, [10, 19]),
    (3267, [81, 40, 27]),
    (83, [17, 5]),
    (156, [15, 6]),
    (7290, [6, 8, 6, 15]),
    (161011, [16, 10, 13]),
    (192, [17, 8, 14]),
    (21037, [9, 7, 18, 13]),
    (292, [11, 6, 16, 20])
]

def extract_list_from_file(file_path: str) -> Tuple[int, list[int]]:
    return_list = []
 

    with open(file_path) as f:
        for line in f:
            split_line = line.split(":")
            resultat = int(split_line[0])
            number_str = list(map(int, split_line[1][1:].split("\n")[0].split(" ")))
            return_list.append((resultat, number_str))
    return return_list

def get_operators_list(number_of_possibility: int) -> list[list[int]]:
    pass

extract_input = extract_list_from_file("input_day7.txt")
for val in extract_input:
    print(val)