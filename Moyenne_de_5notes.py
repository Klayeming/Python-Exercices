"""
Programme qui demande à l'utilisateur de taper 5 notes et qui affiche leur somme et leur moyenne
"""
Notes = list()
Total = 0
for i in range(5):
    Notes.append(float(input(f"Veuillez saisir la note {i+1} : ")))
    Total += Notes[i]
Moyenne = Total / 5
print(f"La somme des notes est de {Total} et la moyenne est de {Moyenne}")
