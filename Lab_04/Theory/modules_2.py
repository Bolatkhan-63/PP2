import modules_1

modules_1.getname("Maksim")

a=modules_1.person1["age"]
print(a)

#Naming a Module
#Re-naming a Modul

import modules_1 as mx

b = mx.person1["age"]
print(b)

#Built-in Modules
import platform

x = platform.system()
print(x)

#Using the dir() Function (There is a built-in function to list all the function names (or variable names) in a module.)

import platform

y = dir(platform)
print(y)

#Import From Module
from modules_1 import person1

print(person1["age"])
