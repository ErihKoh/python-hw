import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def connection_to_server():
    connection = psycopg2.connect(user='postgres',
                                  password='hellga1408',
                                  host='localhost',
                                  port='5432', )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    return connection


def connection_to_db(db):
    connection = psycopg2.connect(user='postgres',
                                  password='hellga1408',
                                  host='localhost',
                                  port='5432',
                                  database=f'{db}')
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    return connection
