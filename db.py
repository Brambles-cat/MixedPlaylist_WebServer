import sqlite3
from sqlite3 import Error
from sqlite3 import Connection

def create_table(conn: Connection, create_table_sql: str):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(data: tuple, keepConnectionOpen= False, connection=None) -> Connection | None:
    conn: Connection = sqlite3.connect("saved_playlists.db", check_same_thread=False) if connection is None else connection
    
    sql = ''' INSERT INTO test(id,owner_id,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    
    if keepConnectionOpen:
        return conn
    
    conn.close()

def get_playlist(id: str) -> tuple:
    conn: Connection = sqlite3.connect("saved_playlists.db", check_same_thread=False)

    sql = ''' SELECT * FROM test WHERE id = ? LIMIT 1'''
    cur = conn.cursor()
    return cur.execute(sql, (id,)).fetchone()

if __name__ == '__main__':

    create_table_test = """ CREATE TABLE IF NOT EXISTS test (
                                        id PRIMARY KEY,
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
    
    conn: Connection = sqlite3.connect("saved_playlists.db", check_same_thread=False)
    create_table(conn, create_table_test)
    conn.commit()
    insert_data((1029, "meow", "some title idk", None, None, None, None, None, None, None, None, None))
    