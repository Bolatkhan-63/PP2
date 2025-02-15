#Local scpoe 
def myfunc():
    x = 300
    print(x)

myfunc()

#Function Inside Function
def myfunc2():
  x = 400
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc2()

#Global Scope
x = 100

def myfunc():
  print(x)

myfunc()

print(x)

#Naming Variables
x = 70000

def myfunc():
  x = 20
  print(x)

myfunc()

print(x)

#Global Keyword
def myfunc():
    global x
    x=500

myfunc()

print(x)

#Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

