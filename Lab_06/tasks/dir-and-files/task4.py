import os

def first_method(path):
    f = open(path, "r")
    line_sum = 0
    for line in f:
        line_sum += 1
    
    print(line_sum)

def second_method(path):
    f = open(path, "r")
    line_sum = 0
    while f.readline():
        line_sum +=1
    f.close()
    print(line_sum)


path = r"C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_06\tasks\dir-and-files\file_for_4_task"

first_method(path)
second_method(path)
