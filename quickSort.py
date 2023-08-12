# quickSort.py contains the quickSort functions for sorting the stars by their name, temperature, and distance.
'''The quick sort algorithm selects an element from the list to serve as a pivot.
All the elements are then re-arranged around the pivot: elements less than the pivot are moved to its left,
and elements greater than the pivot are moved to its right.
This operation is known as partitioning.
After partitioning, the pivot is in its final position. 
This is the "divide" part of the algorithm: the pivot element is in the correct spot,
and the elements on either side of it form two sublists that can be sorted independently.
The quick sort algorithm then recurses on the two sublists. This is the "conquer" part.'''

def quickSortTemp(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    smallerThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for star in list:
        if star.temperature < pivot.temperature:
            smallerThanPivot.append(star)
        elif star.temperature == pivot.temperature:
            equalToPivot.append(star)
        elif star.temperature > pivot.temperature:
            greaterThanPivot.append(star)

    return quickSortTemp(smallerThanPivot) + equalToPivot + quickSortTemp(greaterThanPivot)


def quickSortDistance(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    smallerThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for star in list:
        if star.distance < pivot.distance:
            smallerThanPivot.append(star)
        elif star.distance == pivot.distance:
            equalToPivot.append(star)
        elif star.distance > pivot.distance:
            greaterThanPivot.append(star)

    return quickSortDistance(smallerThanPivot) + equalToPivot + quickSortDistance(greaterThanPivot)
# code based off of https://www.geeksforgeeks.org/python-program-for-quicksort/