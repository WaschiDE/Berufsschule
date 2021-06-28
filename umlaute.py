eingabe=input("Gib einen tollen Text ein \n").casefold()

ausgabe=[]
ausgabe2=[]

if ("a" or "A") in eingabe:
    ausgabe.append("a")
if ("e" or "E") in eingabe:
    ausgabe.append("e")
if ("i" or "I") in eingabe:
    ausgabe.append("i")
if ("o" or "O") in eingabe:
    ausgabe.append("o")
if ("u" or "U") in eingabe:
    ausgabe.append("u")
print("Der Text war:\n '",eingabe,"'\nFolgende Vokale sind im Text vorhanden: ",ausgabe)

vokale=["a","e","i","o","u"]
for i in range(len(vokale)):
    if vokale[i] in eingabe:
        ausgabe2.append(vokale[i])
print("Der Text war:\n '",eingabe,"'\nFolgende Vokale sind im Text vorhanden: ",ausgabe2)