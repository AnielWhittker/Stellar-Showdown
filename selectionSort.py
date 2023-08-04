# selectionSort.py contains the selection sort algorithm for sorting the list of stars by temperature and distance
'''The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
from the unsorted part and putting it at the beginning of the unsorted part. 
This essentially expands the sorted portion of the array from left to right.'''

def selectionSortTemp(list):
    for i in range(len(list)):
        minIndx = i
        for j in range(i+1, len(list)):
            if list[j].temperature < list[minIndx].temperature:
                minIndx = j
        temp = list[i]
        list[i] = list[minIndx]
        list[minIndx] = temp

    return list

def selectionSortDist(list):
    for i in range(len(list)):
        minIndx = i
        for j in range(i+1, len(list)):
            if list[j].distance < list[minIndx].distance:
                minIndx = j
        temp = list[i]
        list[i] = list[minIndx]
        list[minIndx] = temp
        
    return list