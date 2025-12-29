"""
Docstring for Exercices.mini_calculatrice
faire un programme qui propose different type d'operation 
"""

def calcula(a, b, choix):
    if choix == 1:
       c= a+b
       print(f"L'addition de {a} et {b} est {c}")
    elif choix == 2:
       c= a-b
       print(f"La soustraction de {a} et {b} est {c}")
    elif choix == 3:
       c= a*b
       print(f"La multiplication entre {a} et {b} est {c}")
    elif choix == 4:
       if b != 0:
        c= a/b
        print(f"La division de {a} et {b} est {c}")
       else:
          print("La division par 0 n'existe pas")
    elif choix == 2:
       c= a%b
       print(f"Le modulo de {a} et {b} est {c}")
    else:
       print("Oza vrai..... 🤦")

a = float(input("Veuillez saisr le premier nombre: "))
b = float(input("Veuillez saisr le deuxieme nombre: "))
choix = int(input("Veuillez choisir un operateur parmis ce-dernier:\n1.Addition +\n2.Soustraction -\n3.Multiplication *\n4.Division /\n5.Modulo %\nChoix: "))
calcula(a, b, choix)
