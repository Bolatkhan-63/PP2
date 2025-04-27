from info_database3 import *

conn = open_database()
cur = conn.cursor()

cur.execute("""
    INSERT INTO student (id, name, email, gpa)
    VALUES (%s,%s, %s, %s)
""", (3, "Marat","marat@kz","3.1"))

conn.commit()
cur.close()
close_database()