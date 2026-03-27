"""
Module: Divisor Finder

Finds and displays all divisors of a positive integer.

A divisor of n is any integer d where n % d == 0.
"""

def divisor_nub(nbr):
    """Find and print all divisors of a number."""
    for i in range(1, nbr+1):
        if nbr % i == 0:
            # Print header on first divisor
            if i == 1:
                print(f"Les diviseurs de {nbr} sont:" if nbr > 1 else "Le diviseur de 1 est:")
            print(i)

nbr = int(input("Please write a number: "))
while nbr <= 0:
    nbr = int(input("Please write a positive number: "))
divisor_nub(nbr)