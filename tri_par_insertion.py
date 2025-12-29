def tri_par_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab
# Exemple d'utilisation
nombres = [12, 11, 13, 5, 6]
nombres_tries = tri_par_insertion(nombres)
print("Tableau trié :", nombres_tries)