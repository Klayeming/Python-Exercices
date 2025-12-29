"""
#24 Ecrire un programme qui verifie si un caractere est alphabetique, numerique ou caractere special
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
