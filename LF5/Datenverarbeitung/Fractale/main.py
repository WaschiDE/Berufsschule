import sierpinskiTeppich
from tkinter import *
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        master.title("Frakal-Writer")
        Frame.__init__(self, master)

        # Label
        self.startzahl = Label(master, text="Welche Franktalart soll erstellt werden?"). \
            grid(row=0, sticky=E, padx=10)
        self.startsystem = Label(master, text="Welche Stufe soll erstellt werden?"). \
            grid(row=1, sticky=E, padx=10)

        self.stufe = Entry(master, width=50)
        self.ouputText = Entry(master, state="disabled", width=50)

        self.ouputText.grid(row=2, column=0,columnspan=2)

        self.franktalart = ttk.Combobox(root, values=["Sierpinski-Teppich"])
        self.franktalart.current(0)
        self.franktalart.grid(row=0, column=1)

        self.stufe = ttk.Combobox(root, values=["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        self.stufe.current(0)
        self.stufe.grid(row=1, column=1)

        Button(master, text='Datei Schreiben', width=20, command=self.action).grid(row=3, column=1, sticky=S, pady=4)

    def action(self):
        sierpinskiTeppich.main(self.stufe.get())

        self.ouputText.delete(0, END)
        self.ouputText.config(state="normal", background= "Green")
        self.ouputText.insert(END, "Datei 'Sierpinksi_Teppich_Stufe_" + self.stufe.get() + ".svg' geschrieben!")

# Mainfunktion zum Ausführen der GUI
root = Tk()
app = Application(master=root)
app.mainloop()
