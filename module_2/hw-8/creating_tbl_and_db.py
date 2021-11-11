from psycopg2 import Error, DatabaseError


def creating_db(conn, db):
    try:
        connection = conn()
        cursor = connection.cursor()
        print(cursor)

        cr_db = f'CREATE DATABASE {db}'
        cursor.execute(cr_db)
        print('DB has been created')

    except (Exception, Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection has been closed')


def creating_tbl(conn, db):
    try:
        connection = conn(db)
        cursor = connection.cursor()

        group_tbl = """CREATE TABLE groups
                       (id INT PRIMARY KEY NOT NULL,
                        name_gr VARCHAR(128) NOT NULL);"""

        student_tbl = """CREATE TABLE students(id INT PRIMARY KEY NOT NULL,
                         last_name TEXT NULL,
                         n_gr INT NOT NULL,
                         CONSTRAINT fk_st_gr FOREIGN KEY (n_gr) REFERENCES groups (id)
                             ON DELETE SET NULL
                             ON UPDATE CASCADE)"""

        teacher_tbl = """CREATE TABLE teachers(id INT PRIMARY KEY NOT NULL,
                                 last_name TEXT NULL)"""

        course_and_grade_tbl = """CREATE TABLE courses
                                (id INT NOT NULL,
                                course_name VARCHAR(128)
                                teacher INT NOT NULL,
                                CONSTRAINT fk_tch_cr FOREIGN KEY (teacher) REFERENCES teachers (id),
                                grade INT NOT NULL,
                                date DATE NOT NULL)"""

        courses_and_students = """CREATE TABLE std_crs
                                  (student_id INT NOT NULL,
                                  courses_id INT NOT NULL,
                                  CONSTRAINT fk_std_cr_std FOREIGN KEY (students) REFERENCES teachers (id),
                                  CONSTRAINT fk_std_cr_cr FOREIGN KEY (courses) REFERENCES teachers (id))"""

        cursor.execute(group_tbl)
        cursor.execute(student_tbl)
        cursor.execute(teacher_tbl)
        cursor.execute(course_and_grade_tbl)
        cursor.execute(courses_and_students)
        connection.commit()
        print("Successfully created table")

    except (Exception, Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection has been closed')
