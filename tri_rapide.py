def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    else:
        pivot = tab[len(tab) // 2]
        gauche = [x for x in tab if x < pivot]
        milieu = [x for x in tab if x == pivot]
        droite = [x for x in tab if x > pivot]
        return tri_rapide(gauche) + milieu + tri_rapide(droite)

# Exemple d'utilisation
nombres = [10, 7, 8, 9, 1, 5]
nombres_tries = tri_rapide(nombres)
print("Tableau trié :", nombres_tries)