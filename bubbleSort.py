def bubbleSortTemp(list):
    length = len(list)
    returnList = list[:]
    madeSwap = False

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if returnList[j].temperature > returnList[j + 1].temperature:
                temp = returnList[j]
                returnList[j] = returnList[j + 1]
                returnList[j + 1] = temp

                madeSwap = True

        if madeSwap == False:
            return returnList

    return returnList

def bubbleSortDist(list):
    length = len(list)
    returnList = list[:]
    madeSwap = False

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if returnList[j].distance > returnList[j + 1].distance:
                temp = returnList[j]
                returnList[j] = returnList[j + 1]
                returnList[j + 1] = temp

                madeSwap = True

        if madeSwap == False:
            return returnList

    return returnList