import re

def spl_upper(text):
    list1 = re.split(r"(?=[A-Z])",text)
    return list1

text = "helloWorldAndYou"

print(spl_upper(text))