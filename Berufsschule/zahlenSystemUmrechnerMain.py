from tkinter import *
from tkinter import ttk
# Ersetze Startsystem und Zielsystem Entryfelder durch Auswahlfelder (2-35)


# GUI Klassen erstellung
class Application(Frame):
    def __init__(self, master=None):
        # Metadaten
        master.title("Zahlensystemumrechner")
        Frame.__init__(self, master)

        # Label
        self.startzahl = Label(master, text="Welche Zahl soll umgerechnet werden?").\
            grid(row=0, sticky=E, padx=10)
        self.startsystem = Label(master, text="In welchem Zahlensystem befindet sich die Zahl?").\
            grid(row=1, sticky=E, padx=10)
        self.zielsystem = Label(master, text="In welches Zahlensystem soll die Zahl konvertiert werden?").\
            grid(row=2, sticky=E, padx=10)
        self.platzhalter = Label(master, text=""). \
            grid(row=3, sticky=E, padx=10)
        self.ausgabe = Label(master, text="Die Zahl im neuen Zahlensystem:"). \
            grid(row=4, sticky=E, padx=10)
        self.platzhalter = Label(master, text=""). \
            grid(row=5, sticky=E, padx=10)
        self.rechenweg = Label(master, text="Rechenweg:"). \
            grid(row=5, sticky=W, padx=10)

        # Eingabefelder
        self.startzahl = Entry(master, width=50)
        # self.startsystem = Entry(master, width=50)
        # self.zielsystem = Entry(master, width=50)
        self.ausgabe = Entry(master, width=50)
        self.rechenweg = Text(master, width=75)

        # Comboboxen
        self.startsystem = ttk.Combobox(root, values=["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                                      "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
                                                      "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35"])
        self.startsystem.current(1)
        self.startsystem.grid(row=1, column=1)

        self.zielsystem = ttk.Combobox(root, values=["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                                     "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
                                                     "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35"])
        self.zielsystem.current(1)
        self.zielsystem.grid(row=2, column=1)

        # Button
        Button(master, text='Konvertieren', width=20, command=self.action).grid(row=3, column=1, sticky=S, pady=4)

        # Eingabefelder Grid
        self.startzahl.grid(row=0, column=1)
        self.ausgabe.grid(row=4, column=1)
        self.rechenweg.grid(row=7, column=0, columnspan=2)

    # Buttonaction
    def action(self):
        self.ausgabe.delete(0, END)
        self.rechenweg.delete('1.0', END)
        ausgabewert = zahlenSystemUmrechner.main(
            self.startzahl.get(), self.startsystem.get(), self.zielsystem.get())
        rechenweg = zahlenSystemUmrechner.rechenwegfunktion(
            self.startzahl.get(), self.startsystem.get(), self.zielsystem.get())
        self.ausgabe.insert(END, ausgabewert)
        self.rechenweg.insert(END, rechenweg)


# Mainfunktion zum Ausführen der GUI
root = Tk()
app = Application(master=root)
app.mainloop()
