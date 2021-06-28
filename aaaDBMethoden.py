import sqlite3
import os.path
class datenbankFunktionen:
    def dbAnlegen(datenbankname):
        datenbankname="{name}.db".format(name=datenbankname)
        if not os.path.exists(datenbankname):
            connection = sqlite3.connect(datenbankname)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE personen (nachname TEXT, vorname TEXT, plz TEXT, ort TEXT, strasse TEXT, nr TEXT)''')
            connection.commit()
            connection.close()
            print("Die Datenbank {name} wurde erstellt".format(name=datenbankname))
        else:
            print("Es existiert bereits eine Datenbank mit diesem Namen")
    def dbAbfragen(datenbankname):
        datenbankname = "{name}.db".format(name=datenbankname)
        if os.path.exists(datenbankname):
            connection = sqlite3.connect(datenbankname)
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM personen''')
            data = cursor.fetchall()
            speicher="Inhalt der Datenbank {name}\nMit dem Feldmapping(nachname, vorname, plz, ort, strasse, nr)\n".format(name=datenbankname)
            for row in data:
                speicher = "{speicher}\n{row}".format(speicher=speicher,row=row)
            return(speicher)
            print("Die Abfrage wurde getätigt")
            connection.close()

        else:
            print("{name} ist keine gültige Datenbank!\n")
    def dbEintraghinzufügen(datenbankname,nachname,vorname,plz,ort,strasse,nr):
        datenbankname="{name}.db".format(name=datenbankname)
        if os.path.exists(datenbankname):
            connection = sqlite3.connect(datenbankname)
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO personen VALUES(?,?,?,?,?,?)''',(nachname,vorname,plz,ort,strasse,nr))
            connection.commit()
            connection.close()
            print("Der Eintrag wurde erstellt")
        else:
            print("Die angegebene Datenbank existiert nicht")
