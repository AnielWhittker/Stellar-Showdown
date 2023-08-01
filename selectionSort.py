def selectionSortTemp(list):
    for i in range(len(list)):
        minIndx = i
        for j in range(i+1, len(list)):
            if list[j].temperature < list[minIndx].temperature:
                minIndx = j
        list[i] = list[minIndx]
        list[minIndx] = list[i]

    return list

def selectionSortDist(list):
    for i in range(len(list)):
        minIndx = i
        for j in range(i+1, len(list)):
            if list[j].distance < list[minIndx].distance:
                minIndx = j
        list[i] = list[minIndx]
        list[minIndx] = list[i]

    return list