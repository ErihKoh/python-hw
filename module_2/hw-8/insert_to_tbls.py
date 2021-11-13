from psycopg2 import DatabaseError, Error

from data import group_lst, std_lst, teacher_lst, courses_lst


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

    for i in courses_lst:

        if i == courses_lst[-1]:
            insert_query += f" {i}"
        else:
            insert_query += f" {i},"
    return insert_query


def insert_data(conn, db):
    group_query = helper_insert_groups()
    students_query = helper_insert_students()
    teacher_query = helper_insert_teacher()
    courses_query = helper_insert_courses()

    try:
        connection = conn(db)
        cursor = connection.cursor()

        cursor.execute(group_query)
        cursor.execute(students_query)
        cursor.execute(teacher_query)
        cursor.execute(courses_query)

        connection.commit()

    except (Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if conn:
            cursor.close()
            connection.close()
            print('Connection has been closed')
