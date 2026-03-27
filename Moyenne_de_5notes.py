"""
Module: Average Grade Calculator (5 Grades)

Calculates and displays the sum and average of 5 grades entered by the user.

Formula: Average = (sum of all grades) / 5
"""

Notes = []
Total = 0

# Collection of 5 grades from user
for i in range(5):
    Notes.append(float(input(f"Veuillez saisir la note {i+1} : ")))
    Total += Notes[i]

Moyenne = Total / 5
print(f"La somme des notes est de {Total} et la moyenne est de {Moyenne}")
