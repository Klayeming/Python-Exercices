"""
Calcul et Affiche le voulme d'une sphere
"""
from math import pi
rayon = float(input("veuillez saisir la taille de votre rayon : "))
Volume_sphere = (4*pi*(rayon**3))/3
print(f"Le volume d'une sphere avec pour rayon {rayon} est de {format(Volume_sphere, ".2f")}")