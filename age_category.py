"""
Module: Age Category Classifier

Classifies a person into an age category based on their age:
  - Poussin: 6-7 years
  - Pupille: 8-9 years
  - Minime: 10-11 years
  - Cadet: 12-16 years
"""

valeur = int(input("Entrez votre age : "))
if 6<= valeur <= 7:
    print("Tu es un poussin.")
elif 8<= valeur <= 9:
    print("Tu es une Pupille.")
elif 10<= valeur <= 11:
    print("Tu es un minime.")
elif 12<= valeur <= 16:
    print("Tu es un cadet.")
else:
    print("La categorie n'existe pas.")
