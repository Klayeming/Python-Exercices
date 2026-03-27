"""
Module: String Reversal

Reverses a string and capitalizes the first letter.

Alternative: Use slicing with string[::-1] for the same result.
"""

mot = "Docstring"
chaine = []

# Iterate through string in reverse and collect characters
for lettre in reversed(mot):
    chaine.append(lettre)

# Join characters and capitalize first letter
resultat = "".join(chaine).capitalize()
print(f"Original: {mot}")
print(f"Reversed and capitalized: {resultat}")