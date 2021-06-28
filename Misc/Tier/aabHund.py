from Misc.Tier import Tier
class Hund (Tier):
    def __init__(self,name,alter):
        Tier.__init__(self,name,alter)
        self.geraeusch = "WUFF"
