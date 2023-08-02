def heapifyTemp(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i].temperature < arr[left].temperature:
        largest = left

    if right < n and arr[largest].temperature < arr[right].temperature:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapifyTemp(arr, n, largest)


def heapSortTemp(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapifyTemp(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapifyTemp(arr, i, 0)


def heapifyDist(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i].distance < arr[left].distance:
        largest = left

    if right < n and arr[largest].distance < arr[right].distance:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapifyDist(arr, n, largest)


def heapSortDist(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapifyDist(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapifyDist(arr, i, 0)
