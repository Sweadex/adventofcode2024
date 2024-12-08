l1_e = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
l2_e = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def extract_str_from_file(file_path: str) -> str:
    text = ""
    with open(file_path) as f:
        for line in str.split(f.read(), "\n"):
            text += line
    return text
            

def is_correct_number(txt: str, index: int) -> int:
    for i in range(max(3,len(txt))):
        num = txt[index+i:index+i+1]
        if not num.isdigit():
            return i

def get_mul(txt: str) -> int | None:
    try:
        i = txt.index("mul(") + 4
    except ValueError:
        return None
    
    index_after_first = is_correct_number(txt, i)
    if index_after_first > 0 and txt[i+index_after_first] == ',':
        first_num = int(txt[i:i+index_after_first])
    else:
        return None
        
    i = i+index_after_first+1
    index_after_first = is_correct_number(txt, i)
    if index_after_first > 0 and txt[i+index_after_first] == ')':
        second_num = int(txt[i:i+index_after_first])
    else:
        return None

    return first_num * second_num

def is_do(txt: str, i_mul: int, do: bool) -> bool:
    try:
        i_do = txt.index("do()")
    except ValueError:
        i_do = len(txt)
    try:
        i_dont = txt.index("don't()")
    except ValueError:
        i_dont = len(txt)
    if(i_mul>i_do or i_mul>i_dont) and i_do != i_dont:
        do = i_do<i_dont
    return do

def get_somme_of_all_mult(txt: str, with_do: bool):
    somme_of_mult = 0
    do = True
    while len(txt) > 8:
        try:
            i_mul = txt.index("mul(") + 4
        except ValueError:
            break
        if with_do:
            do = is_do(txt, i_mul, do)
        if (do):
            somme_of_mult += get_mul(txt) or 0
        txt = txt[i_mul:]
    return somme_of_mult

text = extract_str_from_file("input_day3.txt")

print(get_somme_of_all_mult(text, False))
print(get_somme_of_all_mult(text, True))