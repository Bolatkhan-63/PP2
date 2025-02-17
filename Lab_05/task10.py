import re

def func7(text):
    list1 = re.split(r"(?=[A-Z])",text)
    new_list = []
    new_list.append(list1[0].lower())
    for i in range(1,len(list1)):
        word = list1[i].lower()
        new_list.append(word)
    print("_".join(new_list))

text = "helloWorldExample"

func7(text)

        
        