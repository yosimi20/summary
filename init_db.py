import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO login (name, mail) VALUES (?, ?)",
            ('yosi', 'yosi@gmail.com')
            )

cur.execute("INSERT INTO login (name, mail) VALUES (?, ?)",
            ('noam', 'noam@gmail.com')
            )

connection.commit()
connection.close()