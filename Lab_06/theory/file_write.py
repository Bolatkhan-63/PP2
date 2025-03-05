f = open(r"C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_06\theory\demofile2.txt",'a')
f.write("This is a new file")
f.close()


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
