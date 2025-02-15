#Dates
import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
y = datetime.datetime(2020, 5, 17)

print(y)

#The strftime() Method
import datetime

z = datetime.datetime(2018, 6, 1)

print(z.strftime("%B"))
