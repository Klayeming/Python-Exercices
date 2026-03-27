"""
Module: Merge Sort Algorithm

Implements the merge sort (fusion) algorithm for sorting lists of numbers.

Algorithm: Divide array in half recursively, then merge sorted halves.
Time Complexity: O(n log n)
Space Complexity: O(n)
Best for: Large datasets, stable sorting required
"""

def tri_fusion(tab):
    """Sort array using merge sort algorithm.
    
    Args:
        tab (list): List of numbers to sort
    
    Returns:
        list: Sorted list
    """
    if len(tab) <= 1:
        return tab
    # Divide into two halves
    mid = len(tab) // 2
    left_half = tri_fusion(tab[:mid])
    right_half = tri_fusion(tab[mid:])
    # Merge sorted halves
    return fusion(left_half, right_half)

def fusion(left, right):
    """Merge two sorted arrays.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
    
    Returns:
        list: Merged sorted array
    """
    sorted_tab = []
    i = j = 0
    
    # Compare elements from both arrays and add smaller to result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_tab.append(left[i])
            i += 1
        else:
            sorted_tab.append(right[j])
            j += 1
    
    # Add remaining elements
    sorted_tab.extend(left[i:])
    sorted_tab.extend(right[j:])
    
    return sorted_tab

# Example usage
nombres = [38, 27, 43, 3, 9, 82, 10]
nombres_tries = tri_fusion(nombres.copy())
print("Tableau trié :", nombres_tries)