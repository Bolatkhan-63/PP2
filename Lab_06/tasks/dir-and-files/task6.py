import os

folder_name = "Files_A_to_Z"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for element in range(ord("A"),ord("Z")+1):
    open(f"{folder_name}/{chr(element)}.txt","w")