# bitonicSort.py contains the bitonic sort algorithm for sorting the list of stars by temperature and distance.
'''The first step in bitonic sort is to build a bitonic sequence from the input. 
This is done by recursively sorting the input in increasing and decreasing orders to create two bitonic sequences, 
and then merging them.'''

def bitonicMergeTemp(list, low, count, direction):
    if count > 1:
        k = count // 2
        for i in range(low , low + k):
            if (direction == 1 and list[i].temperature > list[i + k].temperature) or (direction == 0 and list[i].temperature < list[i + k].temperature):
                temp = list[i]
                list[i] = list[i + k]
                list[i + k] = temp
        bitonicMergeTemp(list, low, k, direction)
        bitonicMergeTemp(list, low + k, k, direction)

def bitonicSortTemp(list, low, count, direction):
    if count > 1:
        k = count // 2
        bitonicSortTemp(list, low, k, 1)
        bitonicSortTemp(list, low + k, k, 0)
        bitonicMergeTemp(list, low, count, direction)

def bitonicMergeDist(list, low, count, direction):
    if count > 1:
        k = count // 2
        for i in range(low , low + k):
            if (direction == 1 and list[i].distance > list[i + k].distance) or (direction == 0 and list[i].distance < list[i + k].distance):
                temp = list[i]
                list[i] = list[i + k]
                list[i + k] = temp
        bitonicMergeDist(list, low, k, direction)
        bitonicMergeDist(list, low + k, k, direction)


def bitonicSortDist(list, low, count, direction):
    if count > 1:
        k = count // 2
        bitonicSortDist(list, low, k, 1)
        bitonicSortDist(list, low + k, k, 0)
        bitonicMergeDist(list, low, count, direction)