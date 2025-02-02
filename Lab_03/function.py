def my_function():
    print("Hello from a function")

my_function()

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function2(*kids):
    print("The youngest child is " + kids[2])


my_function2("Lina","Abosh","Nazym")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
# ** before the parameter name in the function definition.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)

#Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

