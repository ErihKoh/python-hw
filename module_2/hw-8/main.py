from connection_to_db import connection_to_db, connection_to_server
from creating_tbl_and_db import creating_db, creating_tbl
from insert_to_tbls import insert_data

if __name__ == '__main__':
    name_db = 'courses'
    creating_db(connection_to_server, name_db)
    creating_tbl(connection_to_db, name_db)
    insert_data(connection_to_db, name_db)
