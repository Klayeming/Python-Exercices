"""
Module: Euclidean Distance Calculator

Calculates and displays the Euclidean distance between two 2D points.

Formula: d = sqrt((x2-x1)² + (y2-y1)²)
"""
from math import sqrt

Xa = float(input("Veuillez saisir le coordonnée X du point A : "))
Ya = float(input("Veuillez saisir le coordonnée Y du point A : "))
Xb = float(input("Veuillez saisir le coordonnée X du point B : "))
Yb = float(input("Veuillez saisir le coordonnée Y du point B : "))
AB = sqrt(((Xb -Xa)**2)+((Yb-Ya)**2))
print(f"La distance entre le point A de coordonnées({Xa,Ya} et le point B de coordonnées({Xb,Yb}) est {format(AB,".2f")}) ")