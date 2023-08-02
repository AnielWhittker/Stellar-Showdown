def quickSortTemp(list):
    pivot = list[len(list) // 2]

    smallerThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for i in list:
        if list[i].temperature < pivot.temperature:
            smallerThanPivot.append(list[i])

        elif list[i].temperature == pivot.temperature:
            equalToPivot.append(list[i])

        elif list[i].temperature > pivot.temperature:
            greaterThanPivot.append(list[i])

    return quickSortTemp(smallerThanPivot) + equalToPivot + quickSortTemp(greaterThanPivot)


def quickSortDistance(list):
    pivot = list[len(list) // 2]

    smallerThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for i in list:
        if list[i].distance < pivot.distance:
            smallerThanPivot.append(list[i])

        elif list[i].distance == pivot.distance:
            equalToPivot.append(list[i])

        elif list[i].distance > pivot.distance:
            greaterThanPivot.append(list[i])

    return quickSortTemp(smallerThanPivot) + equalToPivot + quickSortTemp(greaterThanPivot)