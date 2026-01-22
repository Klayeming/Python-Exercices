"""
#29 Ecrire un programme qui calcul le factorielle d'un nombre
"""
def check(n):
    while n < 0:
        n=int(input("Veuillez saisir un nombre positif: "))
        if n > 0:
            return n
            break
def factorielle(n):
    fact = 1
    if n==0:
        pass
    else:
        for i in range(2, n+1):
            fact = fact * i
    print(f"Le factorielle de {n}! est {format(fact, ".0f")}")

n = check(int(input("Veuillez saisir le nombre: "))) 
factorielle(n)