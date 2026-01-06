"""
#30Ecrire un programme qui calcul la somme carre des n premier nombre 
"""
def Scarre_impair(n):
    s = 0
    i = 1
    compte = 0
    while True:
        if i%2 != 0:
            s = s + i**2
            compte +=1
        if compte==n:
            break
        i += 1
    print(f"La somme des carrées des {n} premeirs entiers impairs est {s}" if n>1 else f"La somme carrée du premier entiers impair est {s}")

n = int(input("Veuillez saisir un entier: "))
Scarre_impair(n)