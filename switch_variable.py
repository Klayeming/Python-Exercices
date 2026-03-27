"""
Module: Variable Swapper

Swaps the values of two variables using a temporary variable.

Method: Use a temporary variable (C) to store one value while exchanging.
"""

A = int(input("veuillez saisir l'entier A : "))
B = int(input("veuillez saisir l'entier B : "))

# Swap using temporary variable
C = A
A = B
B = C
print(f"Voici l'inverse de la saise : A = {A} et B = {B}")