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
    # Insert multiple records using th more secure "?" method
    albums = [
        ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
        ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
        ('Chronology', 'Chronixx', '01/01/2017', 'Independent', 'MP3'),
        ('Section 8.0', 'Kendricl lamar', '01/01/2012', 'TDE', 'MP3')
    ]
    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
    conn.commit()


if __name__ == '__main__':
    import os
    if not os.path.exists("music_list.db"):
        create_database()

