from typing import Tuple

l1_e = [3, 4, 2, 1, 3, 3]
l2_e = [4, 3, 5, 3, 9, 3]

def extract_list_from_file(file_path: str) -> Tuple[list[int],list[int]]:
    file=open(file_path , "r")
    list_all_number=str.split(file.read())
    file.close()

    liste_1 = []
    liste_2 = []
    for i, val in enumerate(list_all_number):
        if (i%2==0):
            liste_1.append(int(val))
            continue
        liste_2.append(int(val))
    return (liste_1, liste_2)

def get_distance_somme(l1: list[int], l2: list[int]):
    l1.sort()
    l2.sort()
    somme_distance = 0

    for i, val in enumerate(l1):
        somme_distance += abs(l2[i] - val)
    print(f"somme des distance: {somme_distance}")

def get_similarity_score(l1: list[int], l2: list[int]):
    similarity_score = 0
    for val in l1:
        similarity_score += l2.count(val) * val
    print(f"somme de similarité: {similarity_score}")

list_1, list_2 = extract_list_from_file("input_day1.csv")
get_distance_somme(list_1, list_2)
get_similarity_score(list_1, list_2)
