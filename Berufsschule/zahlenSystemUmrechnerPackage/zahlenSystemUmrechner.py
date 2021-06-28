# Funktion rechnet eine Startzahl aus einem Startsystem in ein Zielsystem um
# Eingabe der Startzahl muss als String erfolgen, wenn Startsystem größer als 10
# Implementierung des Start- und Zielsystem nur bis Basis 36
#
#
# Diese Funktion gibt aus einem Startzahl und dem entsprechende Startsystem den Zielwert aus einem angegebenen
# Zielsystem wieder
#
#
# Allgemeine Exceptioncase Behandlung
def main(startzahl, startsystem, zielsystem):
    try:
        return umrechenfunktion(startzahl, startsystem, zielsystem)
    except ValueError:
        ausgabe = "Der eingegebene Startwert wird nicht unterstützt!"
        return ausgabe
    except IndexError:
        ausgabe = "Bitte gib einen Startwert ein!"
        return ausgabe
    except Exception:
        ausgabe = "Unbekannter Fehler aufgetreten!"
        return ausgabe


def umrechenfunktion(startzahl, startsystem, zielsystem):
    dezimalzahl = 0
    i = 0
    ausgabewert = ""
    # Umformung der Inputstring zu Integer
    startsystem = int(startsystem)
    zielsystem = int(zielsystem)
    # Unterscheidung für Zahlensysteme über 10
    if startsystem < 11:
        # Nimm die letzte Stelle der Startzahl und entferne diese von der Startzahl
        # Addiere zum dezimalwert die ausgewertete Zahl mit der Startbasis hoch i
        # Erhöhe i um 1
        # Wenn die Startzahl eine Länge von 0 hat brich die Schleife ab
        while True:
            char = startzahl[-1]
            startzahl = startzahl[:-1]
            dezimalzahl = dezimalzahl + (int(char) * (startsystem ** i))
            i = i + 1
            if len(startzahl) == 0:
                break
    else:
        while True:
            # siehe oben
            # + Ersetzten der Buchstabenwerte mit zugehörigen Int/Decimal-Werten
            char = startzahl[-1]
            startzahl = startzahl[:-1]
            char = buchstabezuziffer(char)
            dezimalzahl = dezimalzahl + (int(char) * (startsystem ** i))
            i = i + 1
            if len(startzahl) == 0:
                break
    # Unterscheidung für Zielsystem ob Basis größer 10
    if zielsystem < 11:
        while True:
            # Modulu der Dezimalzahl ist die neue vorderste Zahl
            # Ganzzahldiffison der Dezimalzhal mit der Basis ergibt den Rechenwert zur Weitergabe in der Schleife
            # Wenn Dezimalwert = 0 wird die Schleife abgebrochen
            ziffer = int(dezimalzahl % zielsystem)
            ausgabewert = "{ziffer}{ausgabe}".format(ziffer=ziffer, ausgabe=ausgabewert)
            dezimalzahl = dezimalzahl // zielsystem
            if dezimalzahl == 0:
                break
    else:
        # siehe oben
        # wenn ziffer > 10 dann zusätzliches Ersetzen mit Buchstabenwert
        while True:
            ziffer = int(dezimalzahl % zielsystem)
            if ziffer > 9:
                ziffer = zifferzubuchstabe(ziffer)

            ausgabewert = "{ziffer}{ausgabe}".format(ziffer=ziffer, ausgabe=ausgabewert)
            dezimalzahl = dezimalzahl // zielsystem
            if dezimalzahl == 0:
                break
    return ausgabewert


# Diese Funktion gibt den Rechenweg als String zurück
# Noch nicht voll Funktionsfähig
# Möglichkeit der Implementierung in der Rechenfunktion
def rechenwegfunktion(startzahl, startsystem, zielsystem):
    rechenweg = "Die Zahl {startzahl} aus dem {startsystem}er-System wird in das {zielsystem}er-System umgewandelt.\n" \
                "Gehe nach folgendem Verfahren vor:\n" \
                "(1) Setze n als Zifferanzahl der Startzahl\n" \
                "(2) Für i=0 bis i=n: Nimm die n-i te Ziffer und Multiplizier diese mit dem \n" \
                "   Startsystem hoch i und addiere die Produkte zu einer Summe. Wenn ein\n" \
                "   Buchstabe als Charakter vorkommt ersetze\n" \
                "   diesen wie folgt: a->10, b->11, c->12, d->13, e->14, f->15, ...\n" \
                "\n" \
                "# Hier wird zeitnah das Rechenbeispiel stehen #\n" \
                "\n" \
                "(3) Nimm den Modulu von {zielsystem} und setze diesen als letzte Ziffer.\n" \
                "(4) Nimm nun die Ganzzahldiffision mit {zielsystem} als Zahl zum Weiterrechnen.\n" \
                "(5) Nimm wieder den Modulu von {zielsystem} von der Ganzzahdiffision und füge diese als\n" \
                "   neue forderste Ziffer ein und fahre mit Schritt 4 weiter.\n" \
                "(6) Wenn die Ganzzahldiffsion 0 ergibt ist die Rechnung fertig.\n" \
                "\n" \
                "# Hier wird zeitnah das Rechenbeispiel stehen #\n" \
                "# Hier wird zeitnah das Ergebnis mit angezeigt # \n" \
                "\n" \
                "Und so einfach sind Zahlensysteme! ;)".\
        format(startzahl=startzahl, startsystem=startsystem, zielsystem=zielsystem)
    return rechenweg


# Diese Funktion ersetzt einen Buchstaben mit dem entsprechenden Zahlenwert über ASCII
def buchstabezuziffer(char):
    if not char.isdigit():
        char = ord(char) - 87
    return char


# Diese Funktion ersetzt einen Wert über 9 mit einem Buchstaben über ASCII
def zifferzubuchstabe(ziffer):
    return chr(ziffer + 87)
