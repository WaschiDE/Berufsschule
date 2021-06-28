file = open("benchmark.csv")
textList = file.readlines()
file.close()
textList.pop(0)
textList.pop(0)
max = ["", 0]
for value in textList:
    datenList = value.split(";")
    prozessor = datenList[1]
    wertungSpiele = datenList[3]
    wertungAnwendung = datenList[4]
    if "Ryzen 9" in prozessor or "Core i9" in prozessor:
        punktePreis = 1
    else:
        if "Ryzen 5" in prozessor or "Ryzen 3" in prozessor or "Core i5" in prozessor:
            punktePreis = 3
        else:
            punktePreis = 2
    punkteQualitaet = round((float(wertungSpiele) + 3 * float(wertungAnwendung)) / 4 / 100 * 3)

    nutzwert = (punktePreis + punkteQualitaet) / 2
    if nutzwert > max[1]:
        max = [prozessor, nutzwert]
print(max[0], " ist mit Nutzert:", max[1], "der beste Prozessor")
