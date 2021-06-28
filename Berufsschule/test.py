from tkinter import *

# Mit der Klasse erstellen Sie einen Codeblock für ein Fenster für Ihre Eingabe
class Application(Frame):
    def __init__(self, master=None):
        master.title("Zahlensystemumrechner")
        Frame.__init__(self, master)

        self.namelabel = Label(master, text="Zahlenumrechner") #Erstellung der Überschrift
        self.namelabel.pack() #Einfügen des Elements
        self.taskLabel = Label(master, text="Geben Sie eine Dezimal- oder HexadezimalZahl ein: ") #Erstellung der Aufforderung
        self.taskLabel.pack()
        self.entrynumber = Entry(master, justify="right", width=8) #Erstellung des Eingabefelds
        self.entrynumber.pack()
        self.resultlabel = Label(master, text="") #Label für das Anzeigen des Ergebnisses
        self.resultlabel.pack()
        self.rechnenhexaButton = Button(master, text="Umrechnen in Hexa", command=self.hexarechnen) #Erstellung des Buttons fürs Hexadezimalsystem
        self.rechnenhexaButton.pack()
        self.rechnendeziButton = Button(master, text="Umrechnen in Dezimal", command=self.dezimalrechnen) #Erstellung des Buttons für Dezimalsystem
        self.rechnendeziButton.pack()

    # Logik die hinter dem Hexabutton steckt
    def hexarechnen(self):
        eingabe = self.entrynumber.get()
        ausgabe = hex(int(eingabe))
        self.resultlabel.config(text="Die Zahl in Hexadezimal umgerechnet lautet: " + str(ausgabe))

    #Logik die hinter dem Dezibutton steckt
    def dezimalrechnen(self):
        eingabe = self.entrynumber.get()
        ausgabe=int(eingabe)
        self.resultlabel.config(text="Die Zahl in Dezimal umgerechnet lautet: " + str(ausgabe))

root = Tk()
app = Application(master=root)
app.mainloop()