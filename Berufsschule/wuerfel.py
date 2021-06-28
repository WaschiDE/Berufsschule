import random
i = 0
'''while True:
    i = i + 1
    augenzahl = random.randrange(1, 7)
    print(augenzahl)
    if augenzahl == 6:
        print("Nach {i} Würfen fiel eine 6".format(i=i))
        break
        '''
augenzahl = 0
for i in range(10):
    augenzahl = sum([augenzahl, random.randrange(1, 7)])
print(f"Nach 10 Würfen sind insgesammt {augenzahl} Augen gefallen".format(augenzahl=augenzahl))
