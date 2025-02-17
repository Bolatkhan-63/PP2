import re

def find_sequences(str):
    part = r'\b[a-z]+_[a-z]+\b'
    return re.findall(part,str)

test_strings = [
    "hello_world is a valid sequence",
    "thisIs_not_valid",
    "python_regex are_powerful",
    "one_two three_four five6six",
    "_underscore_start not_valid",
]

for text in test_strings:
    print(f"'{text}' → {find_sequences(text)}")