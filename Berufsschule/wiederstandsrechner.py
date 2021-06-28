import wiederstandsfunktionen as wf
from tkinter import *
# Ersetze Startsystem und Zielsystem Entryfelder durch Auswahlfelder (2-16)
# Ersetze Textbox durch scrollbare Textbox


class Application(Frame):
    def __init__(self, master=None):
        master.title("Wiederstandbastelrechner")
        Frame.__init__(self, master)

        self.vorhandeneWiederstaende = Label(master, text="Welche Wiederstandsarten sind vorhanden?").\
            grid(row=0, sticky=E, padx=10)
        self.benoetigterWiederstand = Label(master, text="Welcher Wiederstand soll erreicht/angenährt werden?").\
            grid(row=1, sticky=E, padx=10)
        self.zielsystem = Label(master, text="Vorhandene Wiederstände durch KOMMA trennen").\
            grid(row=2, sticky=S, padx=10, columnspan=2)
        self.platzhalter = Label(master, text=""). \
            grid(row=3, sticky=E, padx=10)
        self.platzhalter = Label(master, text=""). \
            grid(row=5, sticky=E, padx=10)
        self.ausgabe = Label(master, text="Ausgabe:"). \
            grid(row=5, sticky=W, padx=10)

        self.vorhandeneWiederstaende = Entry(master, width=50)
        self.benoetigterWiederstand = Entry(master, width=50)
        self.ausgabe = Text(master, width=75)

        Button(master, text='Berechnen', width=20, command=self.action).grid(row=3, column=1, sticky=S, pady=4)

        self.vorhandeneWiederstaende.grid(row=0, column=1)
        self.benoetigterWiederstand.grid(row=1, column=1)
        self.ausgabe.grid(row=7, column=0, columnspan=2)

    def action(self):
        # Leeren der Ausgabe
        self.ausgabe.delete("1.0", END)
        # Führt Methode aus
        ausgabewert = wf.wiederstandwaehlen(self.vorhandeneWiederstaende.get(), self.benoetigterWiederstand.get())
        # Liest jeden Listen Eintrag und Schreibt diesen als Zeile
        for i in ausgabewert:
            self.ausgabe.insert(END, "{i}\n".format(i=i))


root = Tk()
app = Application(master=root)
app.mainloop()
