"""
Module: Sign Checker

Determines whether two numbers have the same sign or different signs.

Logic: If the product of two numbers is positive, they have the same sign.
If the product is negative, they have different signs.
"""

A = int(input("Veuillez saisir la valeur du prémier nombre: "))
B = int(input("Veuillez saisir la valeur du deuxième nombre: "))

if A*B>0:
    print("Les deux nombres ont les même signe ")
else:
    print("Les deux nombres ont des signes differents")
