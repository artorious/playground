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

    # insert multiple records using the more secure "?" method
    albums = [
        ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
        ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
        ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
        ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')
    ]

    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
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

def delete_artist(artist):
    """ Delete an artist from the database """
    conn = sqlite3.connect("music_list.db")
    cursor = conn.cursor()

    sql = "DELETE FROM albums WHERE artist = ?"
    cursor.execute(sql, [(artist)])
    conn.commit()
    cursor.close()
    conn.close()



if __name__ == '__main__':
    import os
    if not os.path.exists("music_list.db"):
        create_database()
    
    print(select_all_albums('Andy Hunter'))
    delete_artist('Andy Hunter')
    print(select_all_albums('Andy Hunter'))

