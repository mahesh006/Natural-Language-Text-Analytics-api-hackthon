import sqlite3

#CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT, analysis real)"
CREATE_TABLEss = '''CREATE TABLE IF NOT EXISTS entries
                    (content TEXT, date TEXT)'''


CREATE_ENTRYss = "INSERT INTO entries VALUES (?, ?)"
RETRIEVE_ENTRIESss = "SELECT * FROM entries"


def create_tablee():
    with sqlite3.connect("data2.db") as connection:
        connection.execute(CREATE_TABLEss)


def create_entryss(content, date):
    with sqlite3.connect("data2.db") as connection:
        connection.execute(CREATE_ENTRYss, (content, date))


def retrieve_entriee():
    with sqlite3.connect("data2.db") as connection:
        cursor = connection.cursor()
        cursor.execute(RETRIEVE_ENTRIESss)
        return cursor.fetchall()
