import re 

def chek_word(s):
    return bool(re.search(r'[ab]$',s))


test_strings = [
    "hello world",
    "data",
    "grab",
    "alphabet",
    "cab",
    "area",
    "ab",
    "testa b",
    "baba",
    "football",
]

for s in test_strings:
    print(f"{s} => {chek_word(s)}")
    