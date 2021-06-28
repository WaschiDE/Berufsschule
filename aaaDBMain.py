import aaaDBMethoden as Datenbanke
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        master.title("Datenbankmanager")
        Frame.__init__(self, master)

        self.datenbanknameLbl = Label(master, text="IMMER ANGEBEN! Datenbankname:").grid(row=0,sticky=E,padx=10)
        self.fillerdatenbanknameLbl = Label(master, text="").grid(row=1,sticky=E,padx=10)
        self.nachnameLbl = Label(master, text="Nachname:").grid(row=2,sticky=E,padx=10)
        self.vornameLbl = Label(master, text="Vorname:").grid(row=3,sticky=E,padx=10)
        self.plzLbl = Label(master, text="Postleitzahl:").grid(row=4,sticky=E,padx=10)
        self.ortLbl = Label(master, text="Wohnort:").grid(row=5,sticky=E,padx=10)
        self.strasseLbl = Label(master, text="Straße:").grid(row=6,sticky=E,padx=10)
        self.nrLbl = Label(master, text="Hausnummer:").grid(row=7,sticky=E,padx=10)
        self.fillerausgabeLbl = Label(master, text="").grid(row=8,sticky=E,padx=10)
        self.ausgabeLbl = Label(master, text="Ausgabe:").grid(row=9,sticky=S,padx=10)

        self.datenbankname = Entry(master,width=50)
        self.nachname = Entry(master,width=50)
        self.vorname = Entry(master,width=50)
        self.plz = Entry(master,width=50)
        self.ort = Entry(master,width=50)
        self.strasse = Entry(master,width=50)
        self.nr = Entry(master,width=50)
        self.ausgabe = Text(master, width=100)


        Button(master,text='Anlegen',width=20,command=self.actionanlegen).grid(row=1, column=1, sticky=S, pady=4)
        Button(master, text='Eintragen', width=20, command=self.actioneintragen).grid(row=8, column=1, sticky=S, pady=4)
        Button(master, text='Auslesen', width=20, command=self.actionauslesen).grid(row=10, column=1, sticky=S, pady=4)



        self.datenbankname.grid(row=0, column=1)
        self.nachname.grid(row=2, column=1)
        self.vorname.grid(row=3, column=1)
        self.plz.grid(row=4, column=1)
        self.ort.grid(row=5, column=1)
        self.strasse.grid(row=6, column=1)
        self.nr.grid(row=7, column=1)
        self.ausgabe.grid(row=10, column=0)

    def actionanlegen(self):
        Datenbanke.datenbankFunktionen.dbAnlegen(self.datenbankname.get())
        self.datenbankname.delete(0, END)

    def actioneintragen(self):
        Datenbanke.datenbankFunktionen.dbEintraghinzufügen(self.datenbankname.get(), self.nachname.get(), self.vorname.get(), self.plz.get(), self.ort.get(), self.strasse.get(), self.nr.get())
        self.nachname.delete(0, END)
        self.vorname.delete(0, END)
        self.plz.delete(0, END)
        self.ort.delete(0, END)
        self.strasse.delete(0, END)
        self.nr.delete(0, END)

    def actionauslesen(self):

        name = Datenbanke.datenbankFunktionen.dbAbfragen(self.datenbankname.get())
        self.ausgabe.insert(END,name)
        self.datenbankname.delete(0, END)


     ###nach datenbank anlege Popup bestätigung
    ###nach personen anlagen Popup bestätigung



root=Tk()
app=Application(master=root)
app.mainloop()






'''    
print("Willkommen im Datenbankmanager\n")
while True:
    programm=input("Wollen Sie:\n1)Eine Datenbank anlegen\n2)Eine Datenbank abfragen\n3)Einen Eintrag in einer Datenbank hinzufügen\n")

    if programm == "1":
        datenbankname = input("Geben Sie den Namen an welche Datenbank erstellt werden soll!\n")
        aaaDBMethoden.dbAnlegen(datenbankname)
        print("1")
    else:
        if programm == "2":
            datenbankname = input("Welche Datenbank soll angezeigt werden?\n")
            aaaDBMethoden.dbAbfragen(datenbankname)
        else:
            if programm == "3":
                datenbankname = input("Geben Sie den Namen an welcher Datenbank etwas hinzugefügt werden soll!\n")
                nachname = input("Bitte gib den Nachnamen der Person ein!")
                vorname = input("Bitte gib den Vornamen der Person ein!")
                plz = input("Bitte gib den Postleitzahl des Wohnorts der Person ein!")
                ort = input("Bitte gib den Wohnort der Person ein!")
                strasse = input("Bitte gib die Straße des Wohnorts der Person ein!")
                nr = input("Bitte gib die Hausnummer des Wohnorts der Person ein!")
                aaaDBMethoden.dbEintraghinzufügen(nachname,vorname,plz,ort,strasse,nr)
            else:
                print("Bitte wähle 1,2,3 aus!")'''

##klasse in phyton: TIER
##mit name, alter, METHODE kann laut geben
##in Hauptprogramm testen