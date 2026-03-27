"""
Programme qui demande à l'utilisateur de taper 3 notes et qui calcul et affiche sa  moyenne
avec de mention
"""

def verify(lises):
    n = len(lises)
    for i in range(n):
        if lises[i]>= 0 and lises[i]<=20:
            return True
        else:
            return False



Notes = list()
Total = 0
for i in range(3):
    Notes.append(float(input(f"Veuillez saisir la note {i+1} de l'élève sur 20: ")))
    verification = verify(Notes)
    if verification:
        Total += Notes[i]
    else :
        while not verification:
            Notes.append(float(input(f"Veuillez saisir un nombre entre 0 et 20 pour la note {i+1} de l'élève : ")))
            verification = verify(Notes)
            if verification:
                Total += Notes[i]
                break

Moyenne = Total / 3
if Moyenne > 16 :
    print("Très Bien")
elif 14 < Moyenne <= 16 :
    print("Bien")
elif 12< Moyenne <=14:
    print("Assez Bien")
elif 10 <= Moyenne <= 12:
    print("Passable")
elif 0 <= Moyenne < 10:
    print("insuffisant")

# Documentation updated

# Grade Scale:
#   - 16+: Très Bien (Excellent)
#   - 14-16: Bien (Good) 
#   - 12-14: Assez Bien (Fair)
#  - 10-12: Passable (Acceptable)
#   - 0-10: Insuffisant (Failing)
