"""
Module: Conditional Variable Swap

Swaps the values of two variables based on the sign of their product.

Logic:
  - If A*B > 0 (same sign): Simple swap
  - Otherwise: Set A = sum, B = product
"""

A = int(input("Veuillez saisir la valeur du prémier nombre: "))
B = int(input("Veuillez saisir la valeur du deuxième nombre: "))

if A*B>0:
    C = A
    A = B
    B = C
    print(f"voici la valeur {A} ainsi que la deuxième valeur {B}")


else:
    C = A+B
    D = A*B
    A = C
    B = D
    print(f"voici la valeur {A} ainsi que la deuxième valeur {B}")
