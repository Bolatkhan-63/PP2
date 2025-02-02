x=lambda a:a+10
print(x(5))

# lambda can take any number of arguments
y=lambda a,b: a*b
print(y(5,6))



def function(n):
    return lambda a:a*n

doubler = function(2)
tripler = function(3)

print(doubler(11))
print(tripler(11))


