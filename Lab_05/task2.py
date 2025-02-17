import re

def funct(str):
    isTRUE = r"^ab{2,3}$"
    if re.fullmatch(isTRUE,str):
        return True
    return False


strings = ["a","abb","abb","abf","abbbbbbb","abbbbd"]
for s in strings:
    print(f"'{s}' : '{funct(s)}'")