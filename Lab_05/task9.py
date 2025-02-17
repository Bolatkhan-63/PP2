import re

def space_upper(text):
    list1 = re.split(r"(?=[A-Z])",text)
    return " ".join(list1)

text = "helloWorldAndYou"

print(space_upper(text))