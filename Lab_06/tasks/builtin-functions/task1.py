from functools import reduce

list1 = [1,2,6,6,5]
result = reduce(lambda x, y: x*y,list1)

print("Result is :",result)