from info_database3 import *

conn = open_database()
cur = conn.cursor()

cur.execute("""
    INSERT INTO courses (id, username)
    VALUES (%s,%s)
""", (3, "English"))

conn.commit()
cur.close()
close_database()