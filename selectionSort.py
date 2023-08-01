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