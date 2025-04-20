from info_database1 import *
from print_database import *
import csv

def insert_by_csv(filename):
    conn = open_database()
    cur = conn.cursor()

    with open(filename,newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO phonebook (name,phone) VALUES (%s,%s)",(name,phone))

    conn.commit()
    cur.close()
    close_database()
    print("CSV file is insert")

insert_by_csv(r"C:\Apps_and_more\KBTU_1курс_2семестр\Programming\Lab_10\tasks\Phonebook\contacts.csv")
