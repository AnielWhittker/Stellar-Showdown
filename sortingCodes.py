# merge sort algorithm code snippet
mergeSort = '''def merge(list, start, mid, end):
  left = list[start:mid + 1]
  right = list[mid + 1:end + 1]
  i = 0
  j = 0
  k = start

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      list[k] = left[i]
      i += 1
    else:
      list[k] = right[j]
      j += 1
    k += 1

  while i < len(left):
    list[k] = left[i]
    i += 1
    k += 1

  while j < len(right):
    list[k] = right[j]
    j += 1
    k += 1

def mergeSort(list, start, end):
  if start < end:
    mid = start + (end - start) // 2
    mergeSort(list, start, mid)
    mergeSort(list, mid+1, end)
    merge(list, start, mid, end)'''

# selection sort algorithm code snippet
selectionSort = '''def selectionSort(list):
    for i in range(len(list)):
        minIndx = i
        for j in range(i+1, len(list)):
            if list[j] < list[minIndx]:
                minIndx = j
        list[i] = list[minIndx]
        list[minIndx] = list[i]

    return list'''

# heap sort algorithm code snippet
heapSort = '''def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)'''

# shell sort algorithm code snippet
shellSort = '''def shellSort(list):
    end = len(list)
    gap = end // 2
    returnList = list[:]

    while gap > 0:
        for i in range(gap, end):
            temp = returnList[i]

            j = i

            while j > gap and returnList[j - gap] > temp:
                returnList[j] = returnList[j - gap]

                j = j - gap

            returnList[j] = temp

        gap = gap // 2

    return returnList'''

# bubble sort algorithm code snippet
bubbleSort = '''def bubbleSort(list):
    length = len(list)
    returnList = list[:]
    madeSwap = False

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if returnList[j] > returnList[j + 1]:
                temp = returnList[j]
                returnList[j] = returnList[j + 1]
                returnList[j + 1] = temp

                madeSwap = True

        if madeSwap == False:
            return returnList

    return returnList'''


# quick sort algorithm code snippet
quickSort = '''def quickSortTemp(list):
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

    return quickSortTemp(smallerThanPivot) + equalToPivot + quickSortTemp(greaterThanPivot)'''

# bitonic sort algorithm code snippet
bitonicSort = '''def bitonicMerge(list, low, count, direction):
    if count > 1:
        k = count // 2
        for i in range(low , low + k):
            if (direction == 1 and list[i] > list[i + k]) or (direction == 0 and list[i] < list[i + k]):
                temp = list[i]
                list[i] = list[i + k]
                list[i + k] = temp
        bitonicMerge(list, low, k, direction)
        bitonicMerge(list, low + k, k, direction)

def bitonicSort(list, low, count, direction):
    if count > 1:
        k = count // 2
        bitonicSort(list, low, k, 1)
        bitonicSort(list, low + k, k, 0)
        bitonicMerge(list, low, count, direction)'''

# tim sort algorithm code snippet
timSort = '''# the built in sorting algorithm in python utilizes timsort which is why this is a viable implementation
def timSortTemp(list):
    list.sort(key=lambda x: x.temperature)
    return list'''

# bogo sort algorithm code snippet
bogoSort = '''import random

def checkForTemp(list):
    for i in range(len(list) - 1):
        if list[i].temperature > list[i + 1].temperature:
            return False

    return True'''
