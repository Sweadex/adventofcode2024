from typing import Tuple

l1_e = [7, 6, 4, 2, 1]
l2_e = [1, 2, 7, 8, 9]
l3_e = [9, 7, 6, 2, 1]
l4_e = [1, 3, 2, 4, 5]
l5_e = [8, 6, 4, 4, 1]
l6_e = [1, 3, 6, 7, 9]

TOLERANCE = 1
MIN = 1
MAX = 3

def extract_list_from_file(file_path: str) -> list[list[int]]:
    liste = []
    
    with open(file_path) as f:
        for line in f:
            liste_tmp = []
            for val in str.split(line):
                liste_tmp.append(int(val))
            liste.append(liste_tmp)
    
    return liste

def is_increase(list: list[int], tolerance: int) -> bool:
    if(len(list)<2):
        return False

    # all increase
    for i in range(len(list) - 1):
        if list[i]>=list[i+1]:
            list_cpy, list_cpy2 = get_two_new_list(list, i)
            tolerance -= 1
            if tolerance < 0:
                return False
            #print(list_cpy, "->" ,is_increase(list_cpy, tolerance), is_min_and_max(list_cpy, MIN, MAX))
            #print(list_cpy2, "->" ,is_increase(list_cpy2, tolerance), is_min_and_max(list_cpy, MIN, MAX))
            return ((is_increase(list_cpy, tolerance) and is_min_and_max(list_cpy, MIN, MAX)) or 
                    (is_increase(list_cpy2, tolerance) and is_min_and_max(list_cpy2, MIN, MAX)))

    return is_min_and_max(list, MIN, MAX)

def is_decrease(list: list[int], tolerance: int) -> bool:
    if(len(list)<2):
        return False

    # all decrease
    for i in range(len(list) - 1):
        if list[i]<=list[i+1]:
            list_cpy, list_cpy2 = get_two_new_list(list, i)
            tolerance -= 1
            if tolerance < 0:
                return False
            #print(list_cpy, "->" ,is_decrease(list_cpy, tolerance), is_min_and_max(list_cpy, MIN, MAX))
            #print(list_cpy2, "->" ,is_decrease(list_cpy2, tolerance), is_min_and_max(list_cpy2, MIN, MAX))
            return ((is_decrease(list_cpy, tolerance) and is_min_and_max(list_cpy, MIN, MAX)) or
                    (is_decrease(list_cpy2, tolerance) and is_min_and_max(list_cpy2, MIN, MAX)))

    return is_min_and_max(list, MIN, MAX)

def is_min_and_max(list: list[int], min: int, max: int) -> bool:
    if(len(list)<2):
        return True

    for i in range(len(list) - 1):
        diff = abs(list[i] - list[i+1])
        if diff < min or diff > max:
            return False
    return True

def get_two_new_list(list: list[int], index_to_del: int) -> Tuple[list[int], list[int]]:
    list_cpy = list.copy()
    list_cpy.pop(index_to_del)
    list_cpy2 = list.copy()
    list_cpy2.pop(index_to_del+1)
    return (list_cpy, list_cpy2)

def is_safe(list: list[int], tolerance) -> bool:
    return is_increase(list, tolerance) or is_decrease(list, tolerance)

# exemple
print(is_safe(l1_e, TOLERANCE))
print(is_safe(l2_e, TOLERANCE))
print(is_safe(l3_e, TOLERANCE))
print(is_safe(l4_e, TOLERANCE))
print(is_safe(l5_e, TOLERANCE))
print(is_safe(l6_e, TOLERANCE))

# input (try: 646)
liste = extract_list_from_file("input_day2.csv")
number_of_safe_reports = 0
for val in liste:
    if(is_safe(val, TOLERANCE)):
        number_of_safe_reports += 1
print("Number of safe reports:", number_of_safe_reports)
