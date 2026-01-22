"""
Docstring for python.Exercices.calcul_n_ieme_nombre
#34 Ecrire un programme qui demande un nombre n et qui calcule le n-ieme nombre de la suite U
ou {U0=6; Un+1=4Un+10}
"""
def check(n):
    if n>1:
        return n
    else:
        while n <=1:
            n=int(input("Veuillez saisir un rang > 0: "))
            if n > 1:
                return n
                break
def suite_U(n):
    u = 6
    for i in range(n):
        u = 4*u + 10
    print(f"Le {n} ieme terme de la suite U est: {u}")

n = check(int(input("Veuillez entre un rang superieur à 0: ")))
suite_U(n)

