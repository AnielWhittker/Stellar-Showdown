# heapSort.py contains the heap sort algorithm for sorting the list of stars by temperature and distance.
'''Heap sort works by first transforming the list into a max heap. 
The largest element in the data (the root of the heap) is then swapped with the last element, 
effectively placing it in its correct position in the sorted array. 
The heap size is reduced by one and heapify operation is called on the root node to restore the max heap property.
The last two steps are repeated until the list is sorted.'''
def heapifyTemp(list, n, i):
    largest_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and list[i].temperature < list[left_child].temperature:
        largest_index = left_child

    if right_child < n and list[largest_index].temperature < list[right_child].temperature:
        largest_index = right_child

    if largest_index != i:
        temp = list[i]
        list[i] = list[largest_index]
        list[largest_index] = temp
        heapifyTemp(list, n, largest_index)


def heapSortTemp(list):
    length = len(list)

    for i in range(length // 2 - 1, -1, -1):
        heapifyTemp(list, length, i)

    for i in range(length - 1, 0, -1):
        (list[i], list[0]) = (list[0], list[i])
        heapifyTemp(list, i, 0)


def heapifyDist(list, n, i):
    largest_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and list[i].distance < list[left_child].distance:
        largest_index = left_child

    if right_child < n and list[largest_index].distance < list[right_child].distance:
        largest_index = right_child

    if largest_index != i:
        temp = list[i]
        list[i] = list[largest_index]
        list[largest_index] = temp
        heapifyDist(list, n, largest_index)


def heapSortDist(list):
    length = len(list)

    for i in range(length // 2 - 1, -1, -1):
        heapifyDist(list, length, i)

    for i in range(length - 1, 0, -1):
        (list[i], list[0]) = (list[0], list[i])
        heapifyDist(list, i, 0)

# Code based off of https://www.geeksforgeeks.org/python-program-for-heap-sort/