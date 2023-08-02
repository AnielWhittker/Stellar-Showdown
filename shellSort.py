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