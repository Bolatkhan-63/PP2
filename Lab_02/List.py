#List
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Len is list
print(len(thislist))

#Listd
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Diapazon
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Proverka
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#add new element
thislist3 = ["apple", "banana", "cherry"]
thislist3.append("orange")
print(thislist3)

#delete element
thislist4 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist4.remove("banana")
print(thislist4)

#loop in list
thislist5 = ["apple", "banana", "cherry"]
for x in thislist5:
    print(x)

#sort list
thislist6 = [100, 50, 65, 82, 23]
thislist6.sort()
print(thislist6)


