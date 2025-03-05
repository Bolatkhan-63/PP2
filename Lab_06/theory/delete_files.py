import os

# f = open("file_for_delete.txt", "w")
# f.write("This file will delete")
# os.remove("file_for_delete.txt")


open("demofile5.txt","w")
#os.rmdir("myfolder")
if os.path.exists("demofile5.txt"):
  os.remove("demofile5.txt")
else:
  print("The file does not exist")


os.makedirs("myfolder")
#Delete Folder
os.rmdir("myfolder")
