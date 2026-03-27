"""
Module: Insertion Sort Algorithm

Implements the insertion sort algorithm for sorting lists of numbers.

Algorithm: Build sorted array one item at a time by inserting elements.
Time Complexity: O(n²)
Space Complexity: O(1)
Best for: Small datasets, nearly sorted lists, or online sorting
"""

def tri_par_insertion(tab):
    """Sort array using insertion sort algorithm.
    
    Args:
        tab (list): List of numbers to sort
    
    Returns:
        list: Sorted list
    """
    n = len(tab)
    # Start from second element
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        # Shift elements greater than key one position right
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        # Insert key at correct position
        tab[j + 1] = key
    return tab

# Example usage
nombres = [12, 11, 13, 5, 6]
nombres_tries = tri_par_insertion(nombres.copy())
print("Tableau trié :", nombres_tries)