#For strings len() returns the number of characters:
x = "Hello World!"

print(len(x))

#For tuples len() returns the number of items in the tuple:
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

#For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))



#Class Polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
