"""
Module: Quadratic Equation Solver

Solves quadratic equations of the form: ax² + bx + c = 0

Using the discriminant method:
  Δ = b² - 4ac
  If Δ > 0: Two distinct real solutions
  If Δ = 0: One repeated real solution
  If Δ < 0: No real solutions (complex numbers)
"""
from math import sqrt

def equation_sd(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0
    
    Args:
        a (float): Coefficient of x²
        b (float): Coefficient of x
        c (float): Constant term
    """
    delt = (b**2) - (4*a*c)
    if delt > 0:
        x1 = (-b + sqrt(delt))/(2*a)
        x2 = (-b - sqrt(delt))/(2*a)
        print(f"L'equation a comme solution X1 ={x1} et X2 = {x2}")
    elif delt == 0:
        x = -b/(2*a)
        print(f"L'equation a comme solution X ={x}")
    else:
        print("L'equation est impossible dans l'ensemble R")
    
a = int(input("Veuillez entrer le coefficient a (de x²): "))
b = int(input("Veuillez entrer le coefficient b (de x): "))
c = int(input("Veuillez entrer le coefficient c (constant): "))
equation_sd(a, b, c)
