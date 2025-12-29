def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    mid = len(tab) // 2
    left_half = tri_fusion(tab[:mid])
    right_half = tri_fusion(tab[mid:])
    
    return fusion(left_half, right_half)
def fusion(left, right):
    sorted_tab = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_tab.append(left[i])
            i += 1
        else:
            sorted_tab.append(right[j])
            j += 1
    
    sorted_tab.extend(left[i:])
    sorted_tab.extend(right[j:])
    
    return sorted_tab   
# Exemple d'utilisation
nombres = [38, 27, 43, 3, 9, 82, 10]
nombres_tries = tri_fusion(nombres)
print("Tableau trié :", nombres_tries)