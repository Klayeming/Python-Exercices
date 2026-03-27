"""
Module: Factorial Calculator

Calculates the factorial of a non-negative integer.

Formula: n! = n × (n-1) × (n-2) × ... × 1
Special case: 0! = 1
"""

def check(n):
    """Validate that input is a positive number."""
    while n < 0:
        n = int(input("Veuillez saisir un nombre positif: "))
        if n > 0:
            return n
            break

def factorielle(n):
    """Calculate and display the factorial of n."""
    fact = 1
    if n == 0:
        pass
    else:
        for i in range(2, n+1):
            fact = fact * i
    print(f"Le factorielle de {n}! est {format(fact, '.0f')}")

n = check(int(input("Veuillez saisir le nombre: ")))
factorielle(n)