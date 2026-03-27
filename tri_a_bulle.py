"""
Module: Bubble Sort Algorithm

Implements the bubble sort algorithm for sorting lists of numbers.

Algorithm: Repeatedly swap adjacent elements if they are in wrong order.
Time Complexity: O(n²)
Space Complexity: O(1)
Best for: Small datasets or nearly sorted lists
"""

def tri_a_bulle(tab):
    """Sort array using bubble sort algorithm.
    
    Args:
        tab (list): List of numbers to sort
    
    Returns:
        list: Sorted list
    """
    n = len(tab)
    for i in range(n):
        # Last i elements already in place
        for j in range(0, n-i-1):
            # Swap if elements in wrong order
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

# Example usage
nombres = [64, 34, 25, 12, 22, 11, 90]
nombres_tries = tri_a_bulle(nombres.copy())
print("Tableau trié :", nombres_tries)
