"""
Module: Inhabitant Tax Eligibility Checker

Determines if a person is subject to taxation based on age and gender.

Tax Rules:
  - Men over 20 years old: Taxable
  - Women aged 18-35: Taxable (with higher rate)
  - Others: Tax exempt
"""

def imposition(age, sexe):
    """Check tax eligibility based on age and gender.
    
    Args:
        age (int): Person's age
        sexe (str): Gender ('M' for male, 'F' for female)
    """
    if age > 20 and sexe == "M":
        print("Vous taxable 👮‍♂️")
    elif 18 <= age <= 35 and sexe == "F":
        print("Whaou! Quel taxation ☺️") 
    else:
        print("Merde tu es tellemnt fauché que tu es exempté d'impôt 🤦 ")

age = int(input("Veuillez entrer votre age: "))
print("Choisissez votre sexe:\n 1.Masculin 👨\n 2.Féminin 👩\n")
choix = int(input("Choix: "))
if choix == 1:
    sexe = "M"
elif choix == 2:
    sexe = "F"
else:
    sexe = "Not defined"
    print("Choix invalide")
imposition(age, sexe)