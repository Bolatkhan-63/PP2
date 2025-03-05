def copy(path1,path2):
    file1 = open(path1,"r")
    
    with open(path2,"w") as file2:
        for line in file1:
            file2.write(line)

    file1.close()

copy("file_7-1","file_7-2")

