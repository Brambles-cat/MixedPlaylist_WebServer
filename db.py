import sqlite3
from sqlite3 import Error
from sqlite3 import Connection
import json

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

def set_video(playlist_id: str, vid_data: str, index: int): # maybe susceptible to sql injection and stuff. check later
    sql = f'UPDATE test SET v{index} = ? WHERE id = ? LIMIT 1'

    with sqlite3.connect("saved_playlists.db", check_same_thread=False) as conn:
        cur = conn.cursor()
        cur.execute(sql, (vid_data, playlist_id))
        conn.commit()

def set_videos(playlist_id: str, playlist: list):
    sql = f'UPDATE test SET v1 = ?, v2 = ?, v3 = ?, v4 = ?, v5 = ?, v6 = ?, v7 = ?, v8 = ?, v9 = ?, v10 = ? WHERE id = ? LIMIT 1'

    videos = [json.dumps(video_data) for video_data in playlist]

    for i in range(10 - len(videos)):
        videos.append(None)

    with sqlite3.connect("saved_playlists.db", check_same_thread=False) as conn:
        cur = conn.cursor()
        cur.execute(sql, (*videos, playlist_id))
        conn.commit()

def delete_row(playlist_id):
    sql = f'DELETE FROM test WHERE id = ?'

    with sqlite3.connect("saved_playlists.db", check_same_thread=False) as conn:
        cur = conn.cursor()
        cur.execute(sql, (playlist_id, ))
        conn.commit()

def get_playlist(id: str) -> tuple | None:
    sql = ''' SELECT * FROM test WHERE id = ? LIMIT 1'''

    with sqlite3.connect("saved_playlists.db", check_same_thread=False) as conn:
        cur = conn.cursor()
        fetched_data = cur.execute(sql, (id,)).fetchone()

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
    