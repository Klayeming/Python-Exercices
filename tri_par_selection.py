"""
Module: Selection Sort Algorithm

Implements the selection sort algorithm for sorting lists of numbers.

Algorithm: Find minimum element and place at beginning, repeat for remaining.
Time Complexity: O(n²)
Space Complexity: O(1)
Best for: Small datasets, when memory usage is critical
"""

def tri_par_selection(tab):
    """Sort array using selection sort algorithm.
    
    Args:
        tab (list): List of numbers to sort
    
    Returns:
        list: Sorted list
    """
    n = len(tab)
    for i in range(n):
        # Find minimum element in remaining unsorted portion
        min_idx = i
        for j in range(i+1, n):
            if tab[j] < tab[min_idx]:
                min_idx = j
        # Swap minimum with current position
        tab[i], tab[min_idx] = tab[min_idx], tab[i]
    return tab

# Example usage
nombres = [64, 25, 12, 22, 11]
nombres_tries = tri_par_selection(nombres.copy())
print("Tableau trié :", nombres_tries)