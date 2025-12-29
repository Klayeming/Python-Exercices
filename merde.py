class merde:
    def ___init__(self, mon, nom2):
        self.mon = mon
        self.nom2 = nom2
    
    def getnom(self):
        return self.mon
    
    def setnom(self,nom):
        self.mon = nom

lui = "pop"
lo="va chier"
monp = merde(lui,lo)

print(monp.getnom(), monp.nom2)
monp.setnom("connard")
print(monp.getnom())