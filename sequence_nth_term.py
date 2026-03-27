"""
Module: Sequence N-th Term Calculator

Calculates the n-th term of the sequence:
  U₀ = 6
  Uₙ₊₁ = 4×Uₙ + 10
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

