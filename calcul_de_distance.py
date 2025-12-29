"""
Ecrire un programme qui calcule et affiche la distance entre deux points A et B dont les coordonnées(Xa, Ya)
et (Xb, Yb) sont entrées au clavier comme entiers.
"""
from math import sqrt
Xa = float(input("Veuillez saisir le coordonnée X du point A : "))
Ya = float(input("Veuillez saisir le coordonnée Y du point A : "))
Xb = float(input("Veuillez saisir le coordonnée X du point B : "))
Yb = float(input("Veuillez saisir le coordonnée Y du point B : "))
AB = sqrt(((Xb -Xa)**2)+((Yb-Ya)**2))
print(f"La distance entre le point A de coordonnées({Xa,Ya} et le point B de coordonnées({Xb,Yb}) est {format(AB,".2f")}) ")