from tkinter import *
import sympy as sy

class Application(Frame):
    def __init__(self,master=None):
        master.title("Funktionsrechner")
        Frame.__init__(self, master)

        self.function = Label(master, text="f(x)").grid(row=0,sticky=E,padx=10)


        Button(master, text='Funktion zeichen', width=20, command=self.zeichnenaction).grid(row=1, column=2, sticky=S, pady=4)
        Button(master, text='Nullstellen berechnen', width=20, command=self.berechnenaction).grid(row=1, column=3, sticky=S, pady=4)


        self.ausgabe = Entry(master, width=150)
        self.a = Entry(master, width=50)
        self.b = Entry(master, width=50)
        self.c = Entry(master, width=50)

        self.ausgabe.grid(row=0,column=1,columnspan=5,rowspan=1)
        self.a.grid(row=3, column=2)
        self.b.grid(row=3, column=3)
        self.c.grid(row=3, column=4)

    def zeichnenaction(self):
        funktion="{a}*x*x+{b}*x+{c}".format(a=self.a.get(),b=self.b.get(),c=self.c.get())
        #in einem popupwindow
        sy.plot(funktion)
    def berechnenaction(self):
        a = int(self.a.get())
        b = int(self.b.get())
        c = int(self.c.get())

        x1=((-b+(b*b-4*a*c)**(1/2))/(2*a))
        x2=((-b-(b*b-4*a*c)**(1/2))/(2*a))

        variable=("x1={x1}  x2={x2}".format(x1=x1,x2=x2))
        self.ausgabe.insert(END, variable)

root=Tk()
app=Application(master=root)
app.mainloop()