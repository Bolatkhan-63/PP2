#Regular expression

import re  #We need to import re for RegEx


#search
txt = "The rain in Spain"
x = re.search("Spain", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


#findall
txt2 = "The rain in Spain"
x2 = re.findall("ai", txt2)
print(x2)


#sub
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


#split
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



#txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

print(x.span())
print(x.string)
print(x.group())


