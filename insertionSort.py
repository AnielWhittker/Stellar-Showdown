# insertionSort.py contains the insertion sort algorithm for sorting the list of stars by temperature and distance
'''Insertion sort works by having a sorted and unsorted section in the list. The first element is designated as
being in the sorted section, and then each element after it is placed into the sorted section in the correct order.
Insertion sort is commonly used to sort cards in a hand.'''
def insertionSortTemp(list):
    if len(list) <= 1:
        return

    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key  # Insert the key in the correct position


def insertionSortDist(list):
    if len(list) <= 1:
        return

    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

# Code based off of https://www.geeksforgeeks.org/python-program-for-insertion-sort/#