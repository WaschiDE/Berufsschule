'''
    Code made by Martin Heyne
     - Created on 09.12.2020 -
     - Version 0.1 -
     - Last Update 09.12.2020 -
 '''
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyodbc

cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};User=monty;Password=22Zk@E_GEj;Server=martinheyne.com;Database=d_birthday_project;Port=3306;')


#Carl
#Bananeneistee
#8.0.22
class Application(Frame):
    def __init__(self, master=None):

        master.title("Birthday-Notificator")
        Frame.__init__(self, master)

        # Label
        self.startzahl = Label(master, text="Füge hier einen neun Geburstag ein -> ").\
            grid(row=0, sticky=E, padx=10)
        self.startsystem = Label(master, text="Ändere hier einen vorhandenen Geburstag -> ").\
            grid(row=1, sticky=E, padx=10)
        self.zielsystem = Label(master, text="Lösche einen vorhandenen Geburstag -> ").\
            grid(row=2, sticky=E, padx=10)
        self.zielsystem = Label(master, text="Zeige Geburstage der nächsten Tage -> "). \
            grid(row=3, sticky=E, padx=10)

        # Button
        Button(master, text='Geburstag hinzufügen', width=20, command=self.geburstagHinzufuegen).\
            grid(row=0, column=1, sticky=S, pady=4)
        Button(master, text='Geburstag ändern', width=20, command=self.geburstagAendern).\
            grid(row=1, column=1, sticky=S, pady=4)
        Button(master, text='Geburstag löschen', width=20, command=self.geburstagLoeschen).\
            grid(row=2, column=1, sticky=S, pady=4)
        Button(master, text='Geburstag abfragen', width=20, command=self.geburstagAbfragen). \
            grid(row=3, column=1, sticky=S, pady=4)

# Hinzufuegen
    def geburstagHinzufuegen(self):
        geburstagHinzufuegen = tk.Toplevel(self)
        geburstagHinzufuegen.title("Birthday-Hinzufuegen")
        Label(geburstagHinzufuegen, text="Füge hier einen neuen Geburtstag ein:").\
            grid(row=0, sticky=E, padx=10, columnspan=2)
        Label(geburstagHinzufuegen, text="Vorname:"). \
            grid(row=1, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Nachname:"). \
            grid(row=2, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Geburstdatum:"). \
            grid(row=3, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Format: YYYY-MM-DD"). \
            grid(row=3,column=2, sticky=E, padx=10)

        self.eVorname = Entry(geburstagHinzufuegen).grid(row=1, column=1)
        eNachname = Entry(geburstagHinzufuegen).grid(row=2, column=1)
        eDatum = Entry(geburstagHinzufuegen).grid(row=3, column=1)

        b = Button(geburstagHinzufuegen, text='Hinzufuegen', width=20, command=self.geburstaghinzufuegensql).\
            grid(row=4, column=1, sticky=S, pady=4)


    def geburstaghinzufuegensql(self):
        print("dosomesql")
        print(self.eVorname.get())
        #Prüfung ob datensatz schon vorhanden
        # abfrage nächster freier primärschlüssel
        #INSERT STATEMENT

#Aendern
    def geburstagAendern(self):
        geburstagHinzufuegen = tk.Toplevel(root)
        geburstagHinzufuegen.title("Birthday-Aendern")
        Label(geburstagHinzufuegen, text="Füge hier einen zu ändernden Geburtstag ein:").\
            grid(row=0, sticky=E, padx=10, columnspan=2)
        Label(geburstagHinzufuegen, text="Vorname:"). \
            grid(row=1, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Nachname:"). \
            grid(row=2, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Geburstdatum:"). \
            grid(row=3, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Format: YYYY-MM-DD"). \
            grid(row=3,column=2, sticky=E, padx=10)

        eVorname = Entry(geburstagHinzufuegen).grid(row=1, column=1)
        eNachname = Entry(geburstagHinzufuegen).grid(row=2, column=1)
        eDatum = Entry(geburstagHinzufuegen).grid(row=3, column=1)

        b = Button(geburstagHinzufuegen, text='Ändern', width=20, command=self.geburstagAendernsql).\
            grid(row=4, column=1, sticky=S, pady=4)

    def geburstagAendernsql(self):
        print("dosomesql")
        #Prüfung ob datensatz schon vorhanden
        # abfrage nächster freier primärschlüssel
        #INSERT STATEMENT

#Loeschen
    def geburstagLoeschen(self):
        geburstagHinzufuegen = tk.Toplevel(root)
        geburstagHinzufuegen.title("Birthday-Loeschen")
        Label(geburstagHinzufuegen, text="Füge hier den zu löschenden Geburtstag ein:").\
            grid(row=0, sticky=E, padx=10, columnspan=2)
        Label(geburstagHinzufuegen, text="Vorname:"). \
            grid(row=1, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Nachname:"). \
            grid(row=2, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Geburstdatum:"). \
            grid(row=3, sticky=E, padx=10)
        Label(geburstagHinzufuegen, text="Format: YYYY-MM-DD"). \
            grid(row=3,column=2, sticky=E, padx=10)

        eVorname = Entry(geburstagHinzufuegen).grid(row=1, column=1)
        eNachname = Entry(geburstagHinzufuegen).grid(row=2, column=1)
        eDatum = Entry(geburstagHinzufuegen).grid(row=3, column=1)

        b = Button(geburstagHinzufuegen, text='Löschen', width=20, command=self.geburstagLoeschensql).\
            grid(row=4, column=1, sticky=S, pady=4)

    def geburstagLoeschensql(self):
        print("dosomesql")
        #Prüfung ob datensatz schon vorhanden
        # abfrage nächster freier primärschlüssel
        #INSERT STATEMENT


#Loeschen
    def geburstagAbfragen(self):
        geburstagHinzufuegen = tk.Toplevel(root)
        geburstagHinzufuegen.title("Birthday-Abfragen")
        Label(geburstagHinzufuegen, text="Für die wieviel nächsten Tage sollen Geburstage angezeigt werden?").\
            grid(row=0, sticky=E, padx=10, columnspan=2)
        Label(geburstagHinzufuegen, text="Tage:"). \
            grid(row=1, sticky=E, padx=10)


        eVorname = Entry(geburstagHinzufuegen).grid(row=1, column=1)


        b = Button(geburstagHinzufuegen, text='Abfragen', width=20, command=self.geburstagAbfragensql).\
            grid(row=4, column=1, sticky=S, pady=4)

    def geburstagAbfragensql(self):
        print("dosomesql")
        #Prüfung ob datensatz schon vorhanden
        # abfrage nächster freier primärschlüssel
        #INSERT STATEMENT

# Mainfunktion zum Ausführen der GUI
root = Tk()
app = Application(master=root)
app.mainloop()
