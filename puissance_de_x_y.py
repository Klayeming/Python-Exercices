"""
Module: Power Calculator

Calculates and displays X raised to the power of Y (X^Y).

Formula: Z = X**Y
"""

X = float(input("Veuillez saisir le Premier nombre : "))
Y = float(input("Veuillez saisir le deuxième nombre (exponent) : ")) 
Z = X**Y
print(f"La puissance de {X} au {Y} est {Z}")