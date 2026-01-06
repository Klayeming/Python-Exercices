"""
#28 calculer la somme d'une suite d'exposant
"""

def serie_expo(n):
    s = 0
    for i in range(n+1):
        s = s + (10**i)
    print(f"La somme de la serie de {n} est {format(s, ".0f")}")

n = int(input("Veuillez saisir le nombre: ")) 
serie_expo(n)