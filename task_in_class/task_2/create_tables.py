from info_database3 import *

def create_game_tables():
    conn = open_database()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE,
            email VARCHAR(50),
            gpa FLOAT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses(
            id SERIAL PRIMARY KEY,
            username VARCHAR(50)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollments(
            id SERIAL PRIMARY KEY,
            username VARCHAR(50),
            course_student VARCHAR(50),
            grade FLOAT
        );
    """)

    conn.commit()
    cur.close()
    close_database()
    print("Кестелер сәтті құрылды.")

create_game_tables()
