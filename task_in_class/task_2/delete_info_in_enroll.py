from info_database3 import *


conn = open_database()
cur = conn.cursor()

cur.execute("""
    DELETE FROM enrollments
""")

conn.commit()
cur.close()
close_database()


