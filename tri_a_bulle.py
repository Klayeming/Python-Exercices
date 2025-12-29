def tri_a_bulle(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab
# Exemple d'utilisation
nombres = [64, 34, 25, 12, 22, 11, 90]
nombres_tries = tri_a_bulle(nombres)
print("Tableau trié :", nombres_tries)
