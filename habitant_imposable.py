"""
Docstring for Exercices.habitant_imposable
ecrire un prgramme qui verifie le sexe et l'age ainsi determine si la personne est imposable
"""
def imposition(age, sexe):
    if age >20 and sexe == "M":
        print("Vous taxable 👮‍♂️")
    elif 18<=age<=35 and sexe =="F":
        print("Whaou! Quel taxation ☺️") 
    else :
        print("Merde tu es tellemnt fauché que tu es exempté d'impôt 🤦 ")

age = int(input("Veuillez entrer votre age: "))
print("Choissisez votre sexe votre sexe :\n 1.Masculin 👨\n 2.Féminin 👩\n")
choix = int(input("Choix: "))
if choix == 1:
    sexe = "M"
elif choix == 2:
    sexe = "F"
else:
    print("Mawa pede moko boye")
imposition(age, sexe)