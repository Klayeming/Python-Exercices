def tri_par_selection(tab):
    n = len(tab)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if tab[j] < tab[min_idx]:
                min_idx = j
        tab[i], tab[min_idx] = tab[min_idx], tab[i]
    return tab
# Exemple d'utilisation
nombres = [64, 25, 12, 22, 11]
nombres_tries = tri_par_selection(nombres)
print("Tableau trié :", nombres_tries)