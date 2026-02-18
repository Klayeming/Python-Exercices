"""
#35 Ecrire un programme qui calcul la suite de fibo
"""
def check(n):
    if n>1:
        return n
    else:
        while n <=1:
            n=int(input("Veuillez saisir un rang > 1: "))
            if n > 1:
                return n        
                
def fibo(n):
    upp = 0
    up  = 1
    print("0 1", end=" ")
    for i in range(n-1):
        u = upp + up
        """
        if u > n:
            print(f"Voici les termes de Fibonacci inferieux ou egaux à {n}")
            break
        """
        print(u, end=" ")
        upp = up
        up = u
    

n = check(int(input("Veuillez entre un rang superieur à 1: ")))
fibo(n)