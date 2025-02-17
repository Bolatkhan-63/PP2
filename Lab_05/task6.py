import re

def func(text):
    return re.sub(r'[ ,.]',":",text)

text = "Hello, world. This is a test sentence, with spaces, commas, and dots."

print(func(text))