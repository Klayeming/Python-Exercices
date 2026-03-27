"""
Module: Odd Square Series Sum Calculator

Calculates the sum of squares of the first n odd numbers.

Formula: 1² + 3² + 5² + ... + (2n-1)² = n(2n-1)(2n+1)/3
"""

def Scarre_impair(n):
    """Calculate sum of squares of first n odd numbers."""
    s = 0
    i = 1
    compte = 0
    # Iterate through odd numbers until we reach n of them
    while True:
        if i % 2 != 0:  # Check if number is odd
            s = s + i**2
            compte += 1
        if compte == n:
            break
        i += 1
    plural = "s" if n > 1 else ""
    print(f"La somme des carrées des {n} premeirs entiers impairs est {s}")

n = int(input("Veuillez saisir un entier: "))
Scarre_impair(n)