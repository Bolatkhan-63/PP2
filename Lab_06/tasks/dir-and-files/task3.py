import os


def is_path_exites(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print(
            "directory =",directory,"\n"
            "filename =",filename
        )

    else:
        print("This path do not exits")

path = "C:/Apps_and_more/KBTU_1курс_2семестр/Programming/Lab_06/tasks/dir-and-files"

is_path_exites(path)