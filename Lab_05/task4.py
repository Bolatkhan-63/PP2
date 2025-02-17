import re

def upcase_lowcase(str):
    word = r'\b[A-Z][a-z]+\b'
    return re.findall(word,str)

test_strings = [
    "Hello world This is a Test",
    "Python java CSharp JavaScript",
    "A simple Example but Not_a_match",
    "Regex_is_fun ButThisIsAlsoValid",
    "some words With Capital Start",
    "NoMatchHere lowercase_only"
]

for word in test_strings:
    print(f'{word} => {upcase_lowcase(word)}')