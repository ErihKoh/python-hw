from psycopg2 import Error, DatabaseError


def creating_db(conn, db):
    cr_db = f'CREATE DATABASE {db}'
    try:
        connection = conn()
        cursor = connection.cursor()
        cursor.execute(cr_db)
        print('DB has been created')

    except (Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print('Connection has been closed')


def helper_creating_groups_tbl():
    return """CREATE TABLE groups
                               (id INT PRIMARY KEY NOT NULL,
                                name_gr VARCHAR(128) NOT NULL);"""


def helper_creating_students_tbl():
    return """CREATE TABLE students(id INT PRIMARY KEY NOT NULL,
                                 last_name TEXT NULL,
                                 n_gr INT NOT NULL,
                                 CONSTRAINT fk_st_gr FOREIGN KEY (n_gr) REFERENCES groups (id)
                                     ON DELETE SET NULL
                                     ON UPDATE CASCADE)"""


def helper_creating_teachers_tbl():
    return """CREATE TABLE teachers(id INT PRIMARY KEY NOT NULL,
                                           last_name TEXT NULL)"""


def helper_creating_courses_tbl():
    return """CREATE TABLE courses
                                    (id INT PRIMARY KEY NOT NULL,
                                                course_name VARCHAR(128),
                                                teacher INT NOT NULL,
                                                CONSTRAINT fk_tch_cr FOREIGN KEY (teacher) REFERENCES teachers (id)
                                                    ON DELETE SET NULL
                                                    ON UPDATE CASCADE,
                                                student INT NOT NULL,
                                                CONSTRAINT fk_std_cr FOREIGN KEY (student) REFERENCES students (id)
                                                    ON DELETE SET NULL
                                                    ON UPDATE CASCADE,
                                                grade INT NOT NULL,
                                                date DATE NOT NULL)"""


def creating_tbl(conn, db):
    group_tbl = helper_creating_groups_tbl()
    student_tbl = helper_creating_students_tbl()
    teacher_tbl = helper_creating_teachers_tbl()
    course_and_grade_tbl = helper_creating_courses_tbl()
    try:
        connection = conn(db)
        cursor = connection.cursor()

        cursor.execute(group_tbl)
        cursor.execute(student_tbl)
        cursor.execute(teacher_tbl)
        cursor.execute(course_and_grade_tbl)

        connection.commit()
        print("Successfully created tables")

    except (Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if conn:
            cursor.close()
            connection.close()
            print('Connection has been closed')
