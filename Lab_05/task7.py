import re

def func7(text):
    list1 = re.split("_",text)
    new_list = []
    new_list.append(list1[0])
    for i in range(1,len(list1)):
        word = list1[i].capitalize()
        new_list.append(word)
    print("".join(new_list))

text = "hello_world_example"

func7(text)

        

