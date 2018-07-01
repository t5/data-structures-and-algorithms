"""Implements the quicksort algorithm"""
import random

def quicksort(unsorted):
    """Returns the sorted list

    Average case for time complexity: O(nlog(n))
    Space complexity: O(n)
    """
    
    if len(unsorted) == 1:
        return unsorted
    if not unsorted:
        return []

    lower = []
    upper = []

    p_index = random.randint(0, len(unsorted)-1)
    p_elem = unsorted.pop(p_index)

    for item in unsorted:
        if item < p_elem:
            lower.append(item)
        else:
            upper.append(item)

    return quicksort(lower) + [p_elem] + quicksort(upper)

TEST = [1, 100, 60, 2, 18, 1, 6, 8, 3]
print(quicksort(TEST))
