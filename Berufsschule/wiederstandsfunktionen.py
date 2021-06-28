
def wiederstandwaehlen(vorhandeneWiederstaende, benoetigterWiederstand):
    # Initialisierungen
    # Formatierung des Eingabe Strings zu einer Stringliste
    vorhandeneWiederstaende = list(vorhandeneWiederstaende.split(","))
    # Formatierung des Eingabe Strings zu float
    benoetigterWiederstand = float(benoetigterWiederstand)
    # Startwert zur Initialisierung des ersten Wiederstandwertes
    besterWiederstand = -10000
    # Startzeile für Ausgabe Stringliste
    besterWiederstandAusgabeStartWert = "Die Beste/n Wiederstandskombinationen für {benoetigterWiederstand} Ohm ist/sind:".\
        format(benoetigterWiederstand=benoetigterWiederstand)
    # Initialwerte für Schaltungsarten
    numbern = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    numbern3 = [0, 1, 2, 3]
    numbern2 = [0, 1]
    numbern1 = [0]

    # Start des Wiederstandvergleiches
    while True:
        # Erster Wiederstand
        for i in vorhandeneWiederstaende:
            wiederstand1 = float(i)
            zwischenspeicher = einPassenderWiederstand(wiederstand1)
            for o in numbern1:
                if abs(zwischenspeicher - benoetigterWiederstand) == abs(besterWiederstand - benoetigterWiederstand):
                    besterWiederstand = zwischenspeicher
                    besterWiederstandAusgabe.append(
                        "Wiederstandsanzahl: 1, Wiederstandssumme: {besterWiederstand}, Schaltart: {o}, Wiederstände: a:{i}".format(
                            besterWiederstand=besterWiederstand, o=o, i=i))
                if abs(zwischenspeicher - benoetigterWiederstand) < abs(
                        besterWiederstand - benoetigterWiederstand):
                    besterWiederstand = zwischenspeicher
                    besterWiederstandAusgabe = [besterWiederstandAusgabeStartWert,
                                                "Wiederstandsanzahl: 2, Wiederstandssumme: {besterWiederstand}, Schaltart: {o},Wiederstände: a:{i}".format(
                                                    besterWiederstand=besterWiederstand, o=o, i=i)]
            # Zweiter Wiederstand
            for j in vorhandeneWiederstaende:
                wiederstand2 = float(j)
                zwischenspeicher = zweiPassenderWiederstand(wiederstand1, wiederstand2)
                for o in numbern2:
                    if abs(zwischenspeicher[o] - benoetigterWiederstand) == abs(
                            besterWiederstand - benoetigterWiederstand):
                        besterWiederstand = zwischenspeicher[o]
                        besterWiederstandAusgabe.append(
                            "Wiederstandsanzahl: 2, Wiederstandssumme: {besterWiederstand}, Schaltart: {o}, Wiederstände: a:{i}, b:{j}".format(
                                besterWiederstand=besterWiederstand, o=o, i=i, j=j))
                    if abs(zwischenspeicher[o] - benoetigterWiederstand) < abs(
                            besterWiederstand - benoetigterWiederstand):
                        besterWiederstand = zwischenspeicher[o]
                        besterWiederstandAusgabe = [besterWiederstandAusgabeStartWert,
                                                    "Wiederstandsanzahl: 2, Wiederstandssumme: {besterWiederstand}, Schaltart: {o},Wiederstände: a:{i}, b:{j}".format(
                                                        besterWiederstand=besterWiederstand, o=o, i=i, j=j)]
                # Dritter Wiederstand
                for m in vorhandeneWiederstaende:
                    wiederstand3 = float(m)
                    zwischenspeicher = dreiPassenderWiederstand(wiederstand1, wiederstand2, wiederstand3)
                    for o in numbern3:
                        if abs(zwischenspeicher[o] - benoetigterWiederstand) == abs(
                                besterWiederstand - benoetigterWiederstand):
                            besterWiederstand = zwischenspeicher[o]
                            besterWiederstandAusgabe.append(
                                "Wiederstandsanzahl: 3, Wiederstandssumme: {besterWiederstand}, Schaltart: {o}, Wiederstände: a:{i}, b:{j}, c:{m}".format(
                                    besterWiederstand=besterWiederstand, o=o, i=i, j=j, m=m))
                        if abs(zwischenspeicher[o] - benoetigterWiederstand) < abs(
                                besterWiederstand - benoetigterWiederstand):
                            besterWiederstand = zwischenspeicher[o]
                            besterWiederstandAusgabe = [besterWiederstandAusgabeStartWert,
                                                        "Wiederstandsanzahl: 3, Wiederstandssumme: {besterWiederstand}, Schaltart: {o},Wiederstände: a:{i}, b:{j}, c:{m}".format(
                                                            besterWiederstand=besterWiederstand, o=o, i=i, j=j, m=m)]
                    # Vierter Wiederstand
                    # Vergleicht Abstand von jeden Wert aus Aktueller Liste aus Liste mit benötigten Wiederstand
                    # mit aktuellem besten Abstand
                        # wenn gleich hinzufügen
                        # wenn besser dann ersetzten der gesammten Liste mit neuem Wert
                    for n in vorhandeneWiederstaende:
                        wiederstand4 = float(n)
                        zwischenspeicher = vierPassenderWiederstand(wiederstand1, wiederstand2, wiederstand3, wiederstand4)
                        for o in numbern:
                            if abs(zwischenspeicher[o] - benoetigterWiederstand) == abs(besterWiederstand - benoetigterWiederstand):
                                besterWiederstand = zwischenspeicher[o]
                                besterWiederstandAusgabe.append(
                                    "Wiederstandsanzahl: 4, Wiederstandssumme: {besterWiederstand}, Schaltart: {o}, Wiederstände: a:{i}, b:{j}, c:{m}, d:{n}".format(
                                        besterWiederstand=besterWiederstand, o=o, i=i, j=j, m=m, n=n))

                            if abs(zwischenspeicher[o] - benoetigterWiederstand) < abs(besterWiederstand - benoetigterWiederstand):
                                besterWiederstand = zwischenspeicher[o]
                                besterWiederstandAusgabe = [besterWiederstandAusgabeStartWert,
                                                            "Wiederstandsanzahl: 4, Wiederstandssumme: {besterWiederstand}, Schaltart: {o},Wiederstände: a:{i}, b:{j}, c:{m}, d:{n}".format(
                                                                besterWiederstand=besterWiederstand, o=o, i=i, j=j, m=m, n=n)]
        break
    # Sortieren der Liste nach Wiederstandsanzahl
    besterWiederstandAusgabe = sorted(besterWiederstandAusgabe)
    return besterWiederstandAusgabe


# Wiederstandsrechner bei einem Wiederstand
    # ja ist redundant
def einPassenderWiederstand(wiederstand1):
    return wiederstand1


# Wiederstandsrechner bei zwei Wiederständen
    # entweder Reihe oder Parallel
def zweiPassenderWiederstand(wiederstand1, wiederstand2):
    # 0)Reihe
    wiederstandsumme1 = wiederstand1 + wiederstand2
    # 1)Parallel
    wiederstandsumme2 = parallel(wiederstand1, wiederstand2, 0, 0)
    wiederstandsliste = (wiederstandsumme1, wiederstandsumme2)
    return wiederstandsliste


# Wiederstandsrechner bei drei Wiederständen
def dreiPassenderWiederstand(wiederstand1, wiederstand2, wiederstand3):
    # 0) Reihe
    wiederstandsumme1 = wiederstand1 + wiederstand2 + wiederstand3
    # 1) 1 Reihe und dann 1 und 1 in Parallel
    wiederstandsumme2 = wiederstand1 + parallel(wiederstand2, wiederstand3, 0, 0)
    # 2) 2 und 1 in Parallel
    wiederstandsumme3 = parallel((wiederstand1+wiederstand2), wiederstand3, 0, 0)
    # 3) 1 und 1 und 1 in Parallel
    wiederstandsumme4 = parallel(wiederstand1, wiederstand2, wiederstand3, 0)
    wiederstandsliste = (wiederstandsumme1, wiederstandsumme2, wiederstandsumme3, wiederstandsumme4)
    return wiederstandsliste


# Wiederstandsrechner bei vier Wiederständen
    # Es gibt andere Schlatungsarten die sich aber auf Grund der Kommutativität der Reihenschaltung erübrigen
def vierPassenderWiederstand(wiederstand1, wiederstand2, wiederstand3, wiederstand4):
    # 0)4 in Reihe
    wiederstandsumme1 = wiederstand1 + wiederstand2 + wiederstand3 + wiederstand4
    # 1)2 in Reihe und 2 Parallel
    wiederstandsumme2 = wiederstand1 + wiederstand2 + parallel(wiederstand3, wiederstand4, 0, 0)
    # 2)1 in Reihe und 3 Parallel
    wiederstandsumme3 = wiederstand1 + parallel(wiederstand2, wiederstand3, wiederstand4, 0)
    # 3)1 in Reihe und (1 und 2 in Reihe) in Parallel
    wiederstandsumme4 = wiederstand1 + parallel(wiederstand2, (wiederstand3+wiederstand4), 0, 0)
    # 4)(2 in Reihe und 2 in Reihe)in Parallel
    wiederstandsumme5 = parallel((wiederstand1+wiederstand2), wiederstand3+wiederstand4, 0, 0)
    # 5) (1 und 3 in Reihe)in Parallel
    wiederstandsumme6 = parallel(wiederstand1, (wiederstand2+wiederstand3+wiederstand4), 0, 0)
    # 6) (2 in Parallel)(2 in Parallel)in Reihe
    wiederstandsumme7 = parallel(wiederstand1, wiederstand2, 0, 0)+parallel(wiederstand3, wiederstand4, 0, 0)
    # 7) (2in Reihe und 1 und 1)in Parallel
    wiederstandsumme8 = parallel(wiederstand1, wiederstand2, (wiederstand3+wiederstand4), 0)
    # 8) (4in parallel)
    wiederstandsumme9 = parallel(wiederstand1, wiederstand2, wiederstand3, wiederstand4)
    # Zusammenfügen aller Wiederstände in einer Liste
    wiederstandsliste = (wiederstandsumme1, wiederstandsumme2, wiederstandsumme3, wiederstandsumme4, wiederstandsumme5,
                         wiederstandsumme6, wiederstandsumme7, wiederstandsumme8, wiederstandsumme9)
    return wiederstandsliste


# Parallelschaltungsrechner
    # Berechnung des Wiederstands nach einer Parallelschlatung mit 2-4 Wiederständen
    # Wenn wiederstand 3 und oder 4 nicht vorhanden  setzte diese 0
def parallel(wiederstand1, wiederstand2, wiederstand3, wiederstand4):
    if wiederstand4 == 0:
        if wiederstand3 == 0:
            wiederstandsumme = 1 / ((1 / wiederstand1) + (1 / wiederstand2))
        else:
            wiederstandsumme = 1 / ((1 / wiederstand1) + (1 / wiederstand2) + (1 / wiederstand3))
    else:
        wiederstandsumme = 1/((1/wiederstand1)+(1/wiederstand2)+(1/wiederstand3)+(1/wiederstand4))
    return wiederstandsumme
