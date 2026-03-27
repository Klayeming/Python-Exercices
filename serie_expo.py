"""
Module: Exponential Series Sum Calculator

Calculates the sum of an exponential series with base 10:
  S(n) = 10° + 10¹ + 10² + ... + 10ⁿ

This is a geometric series with first term a=1 and common ratio r=10.
"""

def serie_expo(n):
    """Calculate exponential series sum with base 10."""
    s = 0
    for i in range(n+1):
        s = s + (10**i)
    print(f"La somme de la serie de {n} est {format(s, '.0f')}")

n = int(input("Veuillez saisir le nombre: "))
serie_expo(n)