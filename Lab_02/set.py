#Set
myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#sets
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#add new element
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#join set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

