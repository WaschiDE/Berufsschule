import sympy as sy

##primfaktor zelegung
while True:
    try:
        eingabe=0
        eingabe = int(input("Gib eine Zahl aus die in Primfaktoren zerlegt werden soll:\n"))
    except ValueError:
        print("Das war keine Zahl!")
    if eingabe>1:
        ausgabe="Die Primfaktorzerlegung der Zahl {eingabe} ist: ".format(eingabe=eingabe)
        for key in (sy.factorint(eingabe).keys()):
           ausgabe="{ausgabe}{key}^{value} * ".format(ausgabe=ausgabe,key=key,value=sy.factorint(eingabe).get(key))
        ausgabe=ausgabe[:-2]
        print(ausgabe)
        ##Kontrolle print(sy.factorint(eingabe))
    else:
        print("Gib eine GANZE Zahl ein die größer als 1 ist!")
    if (input("p)rogramm beenden n)ächste Berechnung)")) == "p": break
    eingabe=0