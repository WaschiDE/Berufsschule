import sqlite3
import os.path
try:
    connection = sqlite3.connect('Datenbank.db')
    cursor = connection.cursor()
    ##cursor.execute('''CREATE TABLE personen(name TEXT, vorname TEXT)''')
    n="Heyne"
    v="Martin"
    cursor.execute('''INSERT INTO personen VALUES(?,?)''',(n,v))

    cursor.execute('''SELECT * FROM personen''')

    rows=cursor.fetchall()
    i=0
    for row in rows:
        i=i+1
        if"Martin" in row:
            print("Martin ist in Zeile",i)

    connection.commit()

    connection.close()
except sqlite3.Error :
    print("Something went wrong")


##datei "datenbank"-> mehrere methoden
###anlage abfrage schreiben
###hauptprogramm ^