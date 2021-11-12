from psycopg2 import Error, DatabaseError
from test_data import test_lst, test_list2
from data import group_lst, std_lst, teacher_lst, courses_lst


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

        # course_and_grade_tbl = """CREATE TABLE courses
        #                         (id INT PRIMARY KEY NOT NULL,
        #                         course_name VARCHAR(128),
        #                         teacher INT NOT NULL,
        #                         CONSTRAINT fk_tch_cr FOREIGN KEY (teacher) REFERENCES teachers (id),
        #                         grade INT NOT NULL,
        #                         date DATE NOT NULL)"""

        # courses_and_students = """CREATE TABLE std_crs
        #                           (id INT NOT NULL,
        #                           student_id INT NOT NULL,
        #                           course_id INT NOT NULL,
        #                           CONSTRAINT fk_std_cr_std FOREIGN KEY (student_id) REFERENCES students (id)
        #                               ON DELETE SET NULL
        #                               ON UPDATE CASCADE,
        #                           CONSTRAINT fk_std_cr_cr FOREIGN KEY (course_id) REFERENCES courses (id)
        #                               ON DELETE SET NULL
        #                               ON UPDATE CASCADE)"""

        cursor.execute(group_tbl)
        cursor.execute(student_tbl)
        cursor.execute(teacher_tbl)
        cursor.execute(course_and_grade_tbl)
        # cursor.execute(courses_and_students)
        connection.commit()
        print("Successfully created tables")

    except (Exception, Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection has been closed')


def helper_insert_groups():
    insert_query = "INSERT INTO groups (id, name_gr) VALUES "

    for i in group_lst:

        if i == group_lst[-1]:
            insert_query += f" {i}"
        else:
            insert_query += f" {i},"
    return insert_query


def helper_insert_students():
    insert_query = "INSERT INTO students (id, last_name, n_gr) VALUES "

    for i in std_lst:

        if i == std_lst[-1]:
            insert_query += f" {i}"
        else:
            insert_query += f" {i},"
    return insert_query


def helper_insert_teacher():
    insert_query = "INSERT INTO teachers (id, last_name) VALUES "

    for i in teacher_lst:

        if i == teacher_lst[-1]:
            insert_query += f" {i}"
        else:
            insert_query += f" {i},"
    return insert_query


def helper_insert_courses():
    insert_query = "INSERT INTO courses (id, course_name, teacher, student, grade, date) VALUES "

    for i in test_lst:

        if i == test_lst[-1]:
            insert_query += f" {i}"
        else:
            insert_query += f" {i},"
    return insert_query


# def helper_insert_courses_and_std():
#     insert_query = "INSERT INTO std_crs (id, student_id, course_id) VALUES "
#
#     for i in test_list2:
#
#         if i == test_list2[-1]:
#             insert_query += f" {i}"
#         else:
#             insert_query += f" {i},"
#     return insert_query


def insert_data(conn, db):
    try:
        connection = conn(db)
        cursor = connection.cursor()

        group_query = helper_insert_groups()
        students_query = helper_insert_students()
        teacher_query = helper_insert_teacher()
        courses_query = helper_insert_courses()
        # courses_std_query = helper_insert_courses_and_std()

        cursor.execute(group_query)
        cursor.execute(students_query)
        cursor.execute(teacher_query)
        cursor.execute(courses_query)
        # cursor.execute(courses_std_query)

        connection.commit()

    except (Exception, Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection has been closed')
