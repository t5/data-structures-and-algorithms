"""Sorts first_list list using Mergesort"""

def merge(first_list, second_list):
    """Merges the two lists in order"""

    return_list = []

    while first_list and second_list:
        if first_list[0] < second_list[0]:
            return_list.append(first_list[0])
            first_list.pop(0)
        else:
            return_list.append(second_list[0])
            second_list.pop(0)

    if first_list:
        return_list += first_list
    if second_list:
        return_list += second_list

    return return_list

def mergesort(unsorted_list):
    """Merges using recursion"""

    if len(unsorted_list) == 1:
        return unsorted_list

    return merge(mergesort(unsorted_list[:int(len(unsorted_list)/2)]),
                 mergesort(unsorted_list[int(len(unsorted_list)/2):]))
