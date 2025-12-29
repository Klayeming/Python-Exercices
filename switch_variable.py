"""
un programme qui permet de changer le contenu de deux variable
"""
A = int(input("veuillez saisir l'entier A : "))
B = int(input("veuillez saisir l'entier B : "))

C = A
A = B
B = C
print(f"Voici l'inverse de la saise : A = {A} et B = {B}")