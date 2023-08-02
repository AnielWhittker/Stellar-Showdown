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
