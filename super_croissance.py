"""
Module: Population Growth Comparison

Compares linear growth vs. exponential growth for two cities.

City 1: Linear growth (fixed amount each year)
City 2: Exponential growth (percentage increase each year)
"""

def croissance(nom_ville1, nom_ville2, popu_ville1, popu_ville2):
    """Compare growth until City 2 surpasses City 1 in population.
    
    Args:
        nom_ville1 (str): Name of first city (linear growth)
        nom_ville2 (str): Name of second city (exponential growth)
        popu_ville1 (int): Initial population of city 1
        popu_ville2 (int): Initial population of city 2
    """
    i = 0
    # Linear growth for city 1: +50000 per year
    # Exponential growth for city 2: +8% per year
    while popu_ville1 >= popu_ville2:
        popu_ville1 = popu_ville1 + 50000
        popu_ville2 = popu_ville2 + (popu_ville2 * 0.08)
        i = i + 1
    
    plural = " ans" if i > 1 else " an"
    print(f"La ville de {nom_ville2} depassera la ville {nom_ville1} en population dans {i}{plural}")
    print(f" avec une population de {int(popu_ville2)} contre {int(popu_ville1)}")

nom_ville1 = input("Veuillez saisir le nom de la premiere ville: ")
nom_ville2 = input("Veuillez saisir le nom de la deuxieme ville: ")
popu_ville1 = int(input("Veuillez saisir la population de la premiere ville: "))
popu_ville2 = int(input("Veuillez saisir la population de la deuxieme ville: "))
croissance(nom_ville1, nom_ville2, popu_ville1, popu_ville2)