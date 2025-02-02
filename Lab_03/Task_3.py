#1)
class MyClass:
    def getstring(self):
        self.s=input("Enter a string: ")

    def printString(self):
        print(self.s.upper())
    

do_some=MyClass()
do_some.getstring()
do_some.printString()
        

#2)
class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self,lenght):
        self.lenght=lenght
    def area(self):
        print(self.lenght**2)


area=Shape()
area2=Square(5)

area.area()
area2.area()

#3)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  
        self.width = width   
    def area(self):
        print(self.length * self.width ) 
        
rectangle=Rectangle(5,4)
rectangle.area()

#4)
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        print(math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)) 

p1 = Point(3, 4)
p2 = Point(0, 0)

p1.show()  
p2.show()

p1.move(6, 8)
p1.show()

distance = p1.dist(p2)
f"Distance between p1 and p2: {distance}"


#5)
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Current balance: {self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
    
account = Account("John Doe", 1000)
print(account)

account.deposit(500)   
account.deposit(200)

account.withdraw(300)   
account.withdraw(2000)

print(account)

#6)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20, 23, 29, 30]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)