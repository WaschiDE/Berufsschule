class Tier:
    def __init__(self,name,alter):
        self.name=name
        self.alter=alter
    def lautgeben(self):
        from Misc.Tier import aabKatze
        print("'{geraeusch}'   Ich heiße {name} und bin {alter} alt.".format(name=self.name, alter=self.alter, geraeusch=aabKatze.Katze.geraeschget(self)))
