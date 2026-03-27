"""
Module: Character Classifier

Verifies and classifies a character into one of four categories:
  - Alphabetic letter (a-z, A-Z)
  - Numeric digit (0-9)
  - Special character (punctuation)
  - Unrecognized character
"""
import string

def charactere_verify(char):
#ici on met commence par le languge compare le ascii
#("a" or "A" <=char <= "z" or "Z")
    if char in string.ascii_letters:
        print(f"Le charactere {char} est une lettre alphabetique")
    elif char in string.digits :
        print(f"Le charactere {char} est un nombre numerique ")
    elif char in string.punctuation:
        print(f"Le charactere {char} est un caractere speciale")
    else:
        print(f"Le charactere {char} est non repertorier")

char = input("Veuillez saisir votre caractere: ")
charactere_verify(char)
