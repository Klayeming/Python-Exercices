"""
Docstring for Exercices.annee_bixte
"""
def year_bix(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print(f"L'année {year} est bissextil")
    else:
        print(f"L'année {year} est civile")




year = int(input("Veuillez entre l'année à vérifier: "))
year_bix(year)