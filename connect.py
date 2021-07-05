import sqlite3
from sqlite3 import Error

def initiating_local_db():
    """ Connect to MySQL database """
    conn = sqlite3.connect(r"dbase.db")
    try:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS digital_identity (id integer PRIMARY KEY, 
                                                        name text NOT NULL, 
                                                        username text NOT NULL, 
                                                        password text,
                                                        desc text,
                                                        date_modified text);''')

        cur.execute('''CREATE TABLE IF NOT EXISTS master (id integer PRIMARY KEY,
                                                        masterUser text NOT NULL,
                                                        masterPass text NOT NULL);''')

        #cur.execute("""INSERT INTO master (masterUser, masterPass) VALUES ('master', 'master');""")
        conn.commit()

    except Error as e:
        print(e)

if __name__ == '__main__':
    initiating_local_db()

