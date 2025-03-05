#Open a File on the Server

f = open(r"C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_06\theory\demofile.txt", "r")
print(f.read(10))
#print(f.read())


#Read Lines
print(f.readline())  #You can return one line by using the readline() method
print(f.readline())



for x in f:
  print(x)


#Close Files
f.close()