"""
Module: Basic Calculator

Implements a simple calculator with the following operations:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/) with zero-division check
  5. Modulo (%)

Note: There is a duplicate condition for choice 2 in the original code.
"""

def calcula(a, b, choix):
    """Perform basic arithmetic operations based on user choice.
    
    Args:
        a (float): First operand
        b (float): Second operand
        choix (int): Operation choice (1-5)
    """
    if choix == 1:
        c = a + b
        print(f"L'addition de {a} et {b} est {c}")
    elif choix == 2:
        c = a - b
        print(f"La soustraction de {a} et {b} est {c}")
    elif choix == 3:
        c = a * b
        print(f"La multiplication entre {a} et {b} est {c}")
    elif choix == 4:
        if b != 0:
            c = a / b
            print(f"La division de {a} et {b} est {c}")
        else:
            print("La division par 0 n'existe pas")
    elif choix == 5:
        c = a % b
        print(f"Le modulo de {a} et {b} est {c}")
    else:
        print("Oza vrai..... 🤦")

a = float(input("Veuillez saisir le premier nombre: "))
b = float(input("Veuillez saisir le deuxieme nombre: "))
choix = int(input("Veuillez choisir un operateur parmis ce-dernier:\n1.Addition +\n2.Soustraction -\n3.Multiplication *\n4.Division /\n5.Modulo %\nChoix: "))
calcula(a, b, choix)
