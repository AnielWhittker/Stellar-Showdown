def heapifyTemp(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[i].temperature < list[left].temperature:
        largest = left

    if right < n and list[largest].temperature < list[right].temperature:
        largest = right

    if largest != i:
        (list[i], list[largest]) = (list[largest], list[i])
        heapifyTemp(list, n, largest)


def heapSortTemp(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1):
        heapifyTemp(list, n, i)

    for i in range(n - 1, 0, -1):
        (list[i], list[0]) = (list[0], list[i])
        heapifyTemp(list, i, 0)


def heapifyDist(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[i].distance < list[left].distance:
        largest = left

    if right < n and list[largest].distance < list[right].distance:
        largest = right

    if largest != i:
        (list[i], list[largest]) = (list[largest], list[i])
        heapifyDist(list, n, largest)


def heapSortDist(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1):
        heapifyDist(list, n, i)

    for i in range(n - 1, 0, -1):
        (list[i], list[0]) = (list[0], list[i])
        heapifyDist(list, i, 0)
