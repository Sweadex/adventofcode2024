from typing import Tuple

liste_regle = [
    [47, 53],
    [97, 13],
    [97, 61],
    [97, 47],
    [75, 29],
    [61, 13],
    [75, 53],
    [29, 13],
    [97, 29],
    [53, 29],
    [61, 53],
    [97, 53],
    [61, 29],
    [47, 13],
    [75, 47],
    [97, 75],
    [47, 61],
    [75, 61],
    [47, 29],
    [75, 13],
    [53, 13]
]

le = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]
]

def extract_list_from_file(file_path: str) -> Tuple[list[list[int]], list[list[int]]]:
    rule_list = []
    list = []
    is_rule_list = True
    
    with open(file_path) as f:
        for line in f:
            if line == "\n":
                is_rule_list = False
                continue

            liste_tmp = []
            if is_rule_list:
                for val in str.split(line, "|"):
                    if val == '\n':
                        break
                    liste_tmp.append(int(val))
                rule_list.append(liste_tmp)
            else:
                for val in str.split(line, ","):
                    if val == '\n':
                        break
                    liste_tmp.append(int(val))
                list.append(liste_tmp)
    
    return list, rule_list

def get_list_of_number_after(number_before: int, rule_list: list[list[int]]) -> list[int]:
    list_of_number_after = []
    for val in rule_list:
        if(val[0] == number_before):
            list_of_number_after.append(val[1])
    return list_of_number_after
            

def is_correctly_order(list: list[int], rule_list: list[list[int]]) -> bool:
    for i, number in enumerate(list):
        list_of_number_after = get_list_of_number_after(number, rule_list)
        for number_after in list_of_number_after:
            try:
                index_of_number_after = list.index(number_after)
                if(i>index_of_number_after):
                    return False
            except ValueError:
                pass
    return True

def get_reorder(list: list[int], rule_list: list[list[int]]) -> list[int]:
    edit_list = list.copy()
    for number in edit_list:
        list_of_number_after = get_list_of_number_after(number, rule_list)
        for number_after in list_of_number_after:
            try:
                index = edit_list.index(number)
                index_of_number_after = edit_list.index(number_after)
                if(index>index_of_number_after):
                    edit_list.pop(index)
                    edit_list.insert(index_of_number_after,number)
            except ValueError:
                pass
    return edit_list

def get_number_in_middle(list: list[int]) -> int:
    return list[len(list)//2]

def get_sum_of_ordered_list(list: list[list[int]], rule_list: list[list[int]]) -> int:
    sum = 0
    for val in list:
        if(is_correctly_order(val, rule_list)):
            val_to_add = get_number_in_middle(val)
            sum += val_to_add
    return sum

def get_sum_of_reordered_only_list(list: list[list[int]], rule_list: list[list[int]]) -> int:
    sum = 0
    for val in list:
        if(not is_correctly_order(val, rule_list)):
            val_to_add = get_number_in_middle(get_reorder(val, rule_list))
            sum += val_to_add
    return sum

list_val, rule_list = extract_list_from_file("input_day5.txt")
#print(get_sum_of_ordered_list(list_val, rule_list))
print(get_sum_of_reordered_only_list(list_val, rule_list))