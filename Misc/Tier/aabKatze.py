from Misc.Tier import Tier
class Katze (Tier):
    def __init__(self,name,alter):
        Tier.__init__(self,name,alter)
        self.maeuseGefangen=0
        self.geraeusch="MIAU"
    def geraeschget(self):
        return self.geraeusch
    def mausfangen(self):
        self.maeuseGefangen=self.maeuseGefangen+1
        print("{name} hat {anzahl} Mäuse gefangen".format(name=self.name,anzahl=self.maeuseGefangen))
