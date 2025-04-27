from info_database3 import *
import random


conn = open_database()
cur = conn.cursor()


cur.execute("SELECT name FROM student;")
usernames = [row[0] for row in cur.fetchall()]


cur.execute("SELECT username FROM courses;")
courses = [row[0] for row in cur.fetchall()]

grades = ["85","95","90","89"]


for username in usernames:
    
    for j in courses:
        grade = random.choice(grades)
        cur.execute("""
            INSERT INTO enrollments (username, course_student, grade)
            VALUES (%s, %s,%s);
        """, (username, j, grade))


conn.commit()
cur.close()
close_database()

print("Enrollments толтырылды!")
