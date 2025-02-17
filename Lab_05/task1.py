import re

def funct(str):
    isTRUE = r"^ab*$"
    if re.fullmatch(isTRUE,str):
        return True
    return False


strings = ["a","ab","abb","abf","abbbbbbb","abbbbd"]
for s in strings:
    print(f"'{s}' : '{funct(s)}'")
    