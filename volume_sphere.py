"""
Module: Sphere Volume Calculator

Calculates and displays the volume of a sphere.

Formula: V = (4/3) × π × r³
"""
from math import pi

rayon = float(input("veuillez saisir la taille de votre rayon : "))
Volume_sphere = (4*pi*(rayon**3))/3
print(f"Le volume d'une sphere avec pour rayon {rayon} est de {format(Volume_sphere, ".2f")}")