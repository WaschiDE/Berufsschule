from Tier import Tier
class Fisch (Tier):
    def __init__(self,name,alter):
        Tier.__init__(self,name,alter)
        self.geraeusch = "BLUBB"