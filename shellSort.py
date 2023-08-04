# shellSort.py contains the shell sort algorithm for sorting the list of stars by temperature and distance
'''Shell sort starts by sorting pairs of elements far apart from each other and progressively reducing the gap between elements 
to be compared. At the end of this process, a final pass of insertion sort is performed on the array. 
The interval between the elements (the gap) is calculated based on the sequence used'''

def shellSortTemp(list):
    end = len(list)
    gap = end // 2
    returnList = list[:]

    while gap > 0:
        for i in range(gap, end):
            temp = returnList[i]

            j = i

            while j > gap and returnList[j - gap].temperature > temp.temperature:
                returnList[j] = returnList[j - gap]

                j = j - gap

            returnList[j] = temp

        gap = gap // 2

    return returnList


def shellSortDistance(list):
    end = len(list)
    gap = end // 2
    returnList = list[:]

    while gap > 0:
        for i in range(gap, end):
            temp = returnList[i]

            j = i

            while j > gap and returnList[j - gap].distance > temp.distance:
                returnList[j] = returnList[j - gap]

                j = j - gap

            returnList[j] = temp

        gap = gap // 2

    return returnList

# Code based off of https://www.geeksforgeeks.org/python-program-for-shellsort/