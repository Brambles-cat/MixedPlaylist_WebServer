import sqlite3
from sqlite3 import Error
from sqlite3 import Connection

def create_table(conn: Connection, create_table_sql: str):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def initialize_playlist(data: tuple, keepConnectionOpen=False, connection=None) -> Connection | None:
    conn: Connection = sqlite3.connect("saved_playlists.db", check_same_thread=False) if connection is None else connection
    
    sql = ''' INSERT INTO test(id,owner_id,v1)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    
    if keepConnectionOpen:
        return conn
    
    conn.close()

def update_data(playlist_id: str, vid_data: str, index: int): # super susceptible to sql injection and stuff. CHANGE LATER

    sql = f'UPDATE test SET v{index} = ? WHERE id = ? LIMIT 1'

    conn: Connection = sqlite3.connect("saved_playlists.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute(sql, (vid_data, playlist_id))
    conn.commit()
    conn.close()

def get_playlist(id: str) -> tuple:
    conn: Connection = sqlite3.connect("saved_playlists.db", check_same_thread=False)

    sql = ''' SELECT * FROM test WHERE id = ? LIMIT 1'''
    cur = conn.cursor()
    fetched_data = cur.execute(sql, (id,)).fetchone()
    
    conn.close()
    return fetched_data

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
    initialize_playlist((1029, "meow", "some title idk", None, None, None, None, None, None, None, None, None))
    