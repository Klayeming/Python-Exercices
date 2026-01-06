"""
#27 calculer la somme d'une suite harmonique
"""

def harmonique(n):
    s = 0
    for i in range(1, n+1):
        s = s + (1/i)
    print(f"La somme harmonique de {n} est {format(s, ".2f")}")

n = int(input("Veuillez saisir le nombre: ")) 
harmonique(n)