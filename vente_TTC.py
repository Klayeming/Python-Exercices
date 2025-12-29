"""
Docstring for Exercices.vente_TTC
Ecrire un prgramme qui calcul la tva selon la categorie du produit A, B, C 
"""
def cal_tva(prix, cate, name):
    if cate == "A":
        tva = prix * (7/100)
        prix_ttc = prix + tva
        print(f"Le prix hors taxe est de {prix} et TTC est {prix_ttc} de {name}")
    elif cate == "B":
        tva = prix * (20/100)
        prix_ttc = prix + tva
        print(f"Le prix hors taxe est de {prix} et TTC est {prix_ttc} de {name}")
    elif cate == "C":
        tva = prix * (25/100)
        prix_ttc = prix + tva
        print(f"Le prix hors taxe est de {prix} et TTC est {prix_ttc} de {name}")

name = input("Veuillez entrer le nom de votre produit: ")
prix = int(input("Veuillez entrer le prix hors taxe du produit: "))
print("Selectionnez la categorie de votre produit :\n 1.Catégorie A 🌽\n 2.Catégorie B 🥄\n 3.Catégorie C🚙")
choix = int(input("Choix: "))
if choix == 1:
    cate = "A"
elif choix == 2:
    cate = "B"
elif choix == 3:
    cate == "C"
else:
    print("Oza Vraie ZOBA 🤦")

cal_tva(prix, cate, name)
