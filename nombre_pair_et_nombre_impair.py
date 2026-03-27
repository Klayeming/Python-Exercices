"""
Module: Even/Odd Number Classifier

Determines if a given number is even or odd.

Logic: A number is even if n % 2 == 0, otherwise it's odd.
"""

def pair_or_impair(n):
    """Check if a number is even (pair) or odd (impair)."""
    if (n % 2) == 0:
        print(f"Le nombre {n} est pair")
    else:
        print(f"Le nombre {n} est impair")

n = float(input("Veuillez entre votre nombre: "))
pair_or_impair(n)