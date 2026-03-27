"""
Module: Quicksort Algorithm

Implements the quicksort (tri rapide) algorithm for sorting lists of numbers.

Algorithm: Select pivot, partition around it, recursively sort partitions.
Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n)
Best for: General purpose sorting, large datasets
"""

def tri_rapide(tab):
    """Sort array using quicksort algorithm.
    
    Args:
        tab (list): List of numbers to sort
    
    Returns:
        list: Sorted list
    """
    if len(tab) <= 1:
        return tab
    else:
        # Choose middle element as pivot
        pivot = tab[len(tab) // 2]
        # Partition into three groups
        gauche = [x for x in tab if x < pivot]  # Less than pivot
        milieu = [x for x in tab if x == pivot]  # Equal to pivot
        droite = [x for x in tab if x > pivot]  # Greater than pivot
        # Recursively sort and concatenate
        return tri_rapide(gauche) + milieu + tri_rapide(droite)

# Example usage
nombres = [10, 7, 8, 9, 1, 5]
nombres_tries = tri_rapide(nombres)
print("Tableau trié :", nombres_tries)