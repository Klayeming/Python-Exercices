"""
Docstring for python.Exercices.super_croissance
#33 Ecrire un programme qui deternime la croissance d'une ville
"""

def croissance(nom_ville1, nom_ville2, popu_ville1, popu_ville2):
    i = 0
    while popu_ville1>=popu_ville2:
        popu_ville1 = popu_ville1 + 50000
        popu_ville2 = popu_ville2 + (popu_ville2*0.08)
        i = i+1
    print(f"La ville de {nom_ville2} depassera la ville {nom_ville1} en population dans {i}"+" ans"if i>1 else"an")
    print(f" avec une population de {popu_ville2} contre {popu_ville1} ")

nom_ville1 = input("Veuillez saisir le nom de la premiere ville: ")
nom_ville2 = input("Veuillez saisir le nom de la deuxieme ville: ")
popu_ville1 = int(input("Veuillez saisir le population de la premiere ville: "))
popu_ville2 = int(input("Veuillez saisir le population de la deuxieme ville: "))
croissance(nom_ville1, nom_ville2, popu_ville1, popu_ville2)