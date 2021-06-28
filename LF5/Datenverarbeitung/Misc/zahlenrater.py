import random
zuErratendeZahl = int(input("Gib eine Zahl von 1 bis 100 ein!"))
i = 0
min = 1
max = 101
while True:
    randomzahl = random.randrange(min, max)
    if randomzahl == zuErratendeZahl:
        print(f"Die Zahl {zuErratendeZahl} wurde in {i} Versuchen erraten.".format(zuErratendeZahl=zuErratendeZahl, i=i))
        break
    if randomzahl < zuErratendeZahl:
        print("Die random Zahl {randomzahl} ist kleiner als die zu erratende Zahl {zuErratendeZahl}.".format(randomzahl=randomzahl, zuErratendeZahl=zuErratendeZahl))
        min = randomzahl + 1
        i = i + 1
    if randomzahl > zuErratendeZahl:
        print("Die random Zahl {randomzahl} ist größer als die zu erratende Zahl {zuErratendeZahl}.".format(randomzahl=randomzahl, zuErratendeZahl=zuErratendeZahl))
        max = randomzahl
        i = i + 1
