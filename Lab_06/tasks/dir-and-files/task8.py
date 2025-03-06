import os
open("file for delete","w")

def proverka(path):
    existence,readability,writability,executability = False, False,False,False

    if os.path.exists(path):
        existence = True #бар болу

    if os.access(path, os.R_OK):
        readability = True #оқылу

    if os.access(path, os.W_OK):
        writability = True #жазылу

    if os.access(path, os.X_OK):
        executability = True #орындалу

    if existence and readability and writability and executability ==True:
        return True
    
    return False

def delete_file(path):
    if proverka(path):
        os.remove(path)
        print("I deleted this file: ",path)
    else:
        print("I can not delete file")

path = "file for delete"

delete_file(path)



