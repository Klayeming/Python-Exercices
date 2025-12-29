"""
Docstring for Exercices.equation_du_second_degre
"""
from math import sqrt
def equation_sd(a,b,c):
    delt = (b**2) - (4*a*c)
    if delt>0:
        x1 = (-b + sqrt(delt))/(2*a)
        x2 = (-b - sqrt(delt))/(2*a)
        print(f"L'equation a comme solution X1 ={x1} et X2 = {x2}")
    elif delt == 0:
        x = -b//2*a
        print(f"L'equation a comme solution X ={x}")
    else:
        print("L'equation est impossible dans l'ensemble R")
    
a = int(input("Veuillez entre le coefficient du premier termes: "))
b = int(input("Veuillez entre le coefficient du premier termes: "))
c = int(input("Veuillez entre le coefficient du premier termes: "))
equation_sd(a, b, c)
