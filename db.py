import sqlite3
from sqlite3 import Error
from sqlite3 import Connection

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn


if __name__ == '__main__':
    conn = create_connection("saved_playlists.db")
    curser = conn.cursor()
    
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS test (
                                        id integer PRIMARY KEY,
                                        owner_id NOT NULL,
                                        v1 text NOT NULL,
                                        v2 text,
                                        v3 text,
                                        v4 text,
                                        v5 text,
                                        v6 text,
                                        v7 text,
                                        v8 text,
                                        v9 text,
                                        v10 text
                                    ); """
    
    curser.execute(sql_create_projects_table)
    

