"""Implements the quicksort algorithm"""

import random

def partition(unsorted):
    """Returns the partition index"""

    ind = random.randint(0, len(unsorted)-1)
    p_elem = unsorted.pop(ind)
    lower = []
    upper = []

    for item in unsorted:
        if item < p_elem:
            lower.append(item)
        else:
            upper.append(item)

    p_index = len(lower)
    unsorted[:] = lower + [p_elem] + upper
    return p_index

def quicksort(unsorted):
    """Returns the sorted list"""

    if not unsorted:
        return []
    if len(unsorted) == 1:
        return unsorted

    p_index = partition(unsorted)
    unsorted[:p_index] = quicksort(unsorted[:p_index])
    unsorted[p_index:] = quicksort(unsorted[p_index:])
    return unsorted

TEST = [100, 60, 2, 18, 1, 6, 8, 3]
print(quicksort(TEST))
