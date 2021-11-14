from psycopg2 import Error, DatabaseError

from connection_to_db import connection_to_db


def select_in_db(conn, db, query_str):
    try:
        connection = conn(db)
        cursor = connection.cursor()
        cursor.execute(query_str)
        results = cursor.fetchall()
        records = [tuple(str(item) for item in t) for t in results]
        for row in records:
            print(row)
    except (DatabaseError, Error) as error:
        print('Error', error)
    finally:
        if conn:
            cursor.close()
            connection.close()
            print('Connection has been closed')


if __name__ == '__main__':
    name_db = 'courses'
    print('Средний балл, который преподаватель ставит студенту.')
    query = """SELECT ROUND(AVG(grade), 2)
        FROM courses
        INNER JOIN students ON students.id = courses.student
        INNER JOIN teachers ON teachers.id = courses.teacher
        WHERE students.last_name = 'Edwards' AND teachers.laST_name = 'Curie'"""
    select_in_db(connection_to_db, name_db, query)

    #  5 студентов с наибольшим средним баллом по всем предметам.
    """SELECT ROUND(avg(grade), 2) as avg_grade, last_name
        FROM courses, students
        WHERE student = students.id
        GROUP BY last_name
        ORDER BY avg_grade DESC
        LIMIT 5"""

    # 1 студент с наивысшим средним баллом по одному предмету.
    """SELECT ROUND(avg(grade), 2) as avg_grade, last_name
        FROM courses, students 
        WHERE course_name = 'Math' AND student = students.id
        GROUP BY student, last_name
        ORDER BY avg_grade DESC
        LIMIT 1"""

    #     средний балл в группе по одному предмету.

    """SELECT course_name, avg(grade)
        FROM courses
        WHERE course_name = 'Math' AND
        (student IN(SELECT id
                       FROM students 
                       WHERE n_gr=3))
        GROUP BY course_name"""

    #   Средний балл в потоке.

    """SELECT ROUND(avg(grade), 2)
        FROM courses"""

    #   Какие курсы читает преподаватель.
    """SELECT course_name, teachers.last_name
        FROM courses, teachers
        WHERE teacher = teachers.id AND last_name = 'Plank'
        GROUP BY course_name, last_name"""

    # Список студентов в группе.
    """SELECT name_gr, students.last_name
        FROM groups, students
        WHERE groups.id = students.n_gr AND name_gr = 'Group 1'
        GROUP BY name_gr, students.last_name"""

    # Оценки студентов в группе по предмету.
    """SELECT students.last_name, course_name, grade, name_gr
        FROM students, courses, groups
        WHERE name_gr = 'Group 1' AND course_name = 'Math'
        GROUP BY students.last_name, course_name, grade, name_gr"""

    # Оценки студентов в группе по предмету на последнем занятии.
    """SELECT courses.grade, courses.course_name, 
       courses.date, students.last_name, 
	   groups.name_gr
       FROM courses, students, groups
       WHERE course_name = 'Math' 
            AND date = '2020-12-13' 
            AND groups.name_gr = 'Group 1'
       GROUP BY last_name, grade, date, name_gr, course_name"""

#     Список курсов, которые посещает студент.
    """SELECT courses.course_name, students.last_name
        FROM courses, students
        WHERE students.last_name = 'Edwards'
        GROUP BY course_name, last_name"""

#     Список курсов, которые студенту читает преподаватель.

    """SELECT courses.course_name
        FROM courses
        INNER JOIN teachers ON courses.teacher = teachers.id
        INNER JOIN students ON students.id = courses.student
        WHERE students.last_name = 'Edwards' AND teachers.last_name = 'Plank'
        LIMIT 2"""

    # Средний балл, который преподаватель ставит студенту.
    """SELECT AVG(grade)
        FROM courses
        INNER JOIN students ON students.id = courses.student
        INNER JOIN teachers ON teachers.id = courses.teacher
        WHERE students.last_name = 'Edwards' AND teachers.laST_name = 'Curie'"""

    # Средний балл, который ставит преподаватель.
    """SELECT AVG(grade)
        FROM courses
        INNER JOIN teachers ON teachers.id = courses.teacher
        WHERE teachers.laST_name = 'Plank'"""