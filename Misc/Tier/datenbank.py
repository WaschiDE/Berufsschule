import sqlite3
import os.path

##Öffnet Datenbank, wenn datenbank nicht vorhanden erstellt neue
connection = sqlite3.connect('Datenbank.db')
##Verbindungsobejkt/Zeiger
cursor = connection.cursor()
##Erstellt Tablle in Db
cursor.execute('''CREATE TABLE personen(name TEXT, vorname TEXT)''')
##Erstellt Eintrag in DB
cursor.execute('''INSERT INTO personen VALUES(?,?)''',(n,v))
###execute Methode zur Ausführung von SQL Befehlen
cursor.execute('''SELECT * FROM personen''')
##Operiert Datendankabfrage
rows=cursor.fetchall()
for row in rows:
    print(row)
##Speichert Änderungen
conenction.commit()
##schliest datenbank verbindung
connection.close()