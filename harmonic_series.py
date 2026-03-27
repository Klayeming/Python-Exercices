"""
Module: Harmonic Series Sum Calculator

Calculates the sum of the harmonic series:
  H(n) = 1 + 1/2 + 1/3 + ... + 1/n

The harmonic series grows logarithmically and diverges as n approaches infinity.
"""

def harmonique(n):
    """Calculate harmonic series sum up to n."""
    s = 0
    for i in range(1, n+1):
        s = s + (1/i)
    print(f"La somme harmonique de {n} est {format(s, '.2f')}")

n = int(input("Veuillez saisir le nombre: "))
harmonique(n)