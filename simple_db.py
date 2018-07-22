""" A simple Database script

    Creates a database with some initial data if it doesn't exist already.
    Defines a few functions that allow the user to query the database, delete
    and update rows.
"""
import sqlite3


def create_database():
    """ Create Database with ample entries """
    conn = sqlite3.connect("music_list.db")
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        """CREATE TABLE albums
            (title text, artist text, release_date text, publisher text,
            media_type text)
        """)
    # Insert Some data
    cursor.execute(
        "INSERT INTO albums VALUES "
        "('Glow', 'Andy Hunter', '7/24/2012',"
        "'Xplore Records', 'MP3')")
    # Save data to database
    conn.commit()
    
def select_all_albums(artist):
    """ Query the database for all the albums by a particular artist """
    conn = sqlite3.connect("music_list.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM albums WHERE artist=?"
    cursor.execute(sql, [(artist)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    import os
    if not os.path.exists("music_list.db"):
        create_database()
    
    print(select_all_albums('Chronixx'))

