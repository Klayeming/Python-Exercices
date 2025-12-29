#Structure_conditionnelle_à_choix_multiple___if_..._elif_..._else_...
valeur = int(input("Entrez votre age : "))
if 6<= valeur <= 7:
    print("Tu es un poussin.")
elif 8<= valeur <= 9:
    print("Tu es une Pupille.")
elif 10<= valeur <= 11:
    print("Tu es un minime.")
elif 12<= valeur <= 16:
    print("Tu es un cadet.")
else:
    print("La categorie n'existe pas.")
