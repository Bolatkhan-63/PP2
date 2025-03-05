import os

def list_items(path):
    
    items = os.listdir(path)

    directories = [item for item in items if os.path.isdir(os.path.join(path, item))]

    files = [item for item in items if os.path.isfile(os.path.join(path, item))]

    all_items = items

    print("📂 Тек папкалар:", directories)
    print("📄 Тек файлдар:", files)
    print("📁 Барлығы:", all_items)


list_items(".")  