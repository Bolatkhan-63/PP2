

def append_list(my_list):
    with open("File_for_5","w") as file:
        for element in my_list:
            file.write(element+ " ")

list1 = ["apple", "banana", "cherry"]

append_list(list1)
