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

        cursor.execute(group_tbl)
        cursor.execute(student_tbl)
        connection.commit()
        print("Successfully created table")

    except (Exception, Error, DatabaseError) as error:
        print('Error connection', error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection has been closed')
