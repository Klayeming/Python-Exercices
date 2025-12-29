"""
Docstring for Exercices.nombre_pair_et_nombre_impair
"""
def pair_or_impair(n):
    if (n%2)==0:
        print(f"Le nombre {n} est pair") 
    else:
        print(f"Le nombre {n} est impair") 

n = float(input("Veuillez entre votre nombre: "))
pair_or_impair(n)