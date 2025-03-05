import os

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

    print(
        "existence = ",existence,"\n",
         "readability = ",readability,"\n",
         "writability = ",writability,"\n",
         "executability = ",executability,"\n"
    )

proverka(".")
    