class mer:
    def ___init__(self, mon="lui", nom2="po"):
        self.mon = mon
        self.nom2 = nom2
    def getnom(self):
        return self.mon
    """def setnom(self,nom):
        self.mon = nom"""

lui = "pop"
lo = "va chier"
monp = mer(lui)

print(monp.getnom(), monp.nom2)
"""monp.setnom("connard")"""
print(monp.getnom())