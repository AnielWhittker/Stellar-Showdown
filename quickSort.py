def quickSortTemp(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    smallerThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for star in list:
        if star.temperate < pivot.temperate:
            smallerThanPivot.append(star)
        elif star.temperature == pivot.temperature:
            equalToPivot.append(star)
        elif star.temperature > pivot.temperature:
            greaterThanPivot.append(star)

    return quickSortTemp(smallerThanPivot) + equalToPivot + quickSortTemp(greaterThanPivot)


def quickSortDistance(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    smallerThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for star in list:
        if star.distance < pivot.distance:
            smallerThanPivot.append(star)
        elif star.distance == pivot.distance:
            equalToPivot.append(star)
        elif star.distance > pivot.distance:
            greaterThanPivot.append(star)

    return quickSortDistance(smallerThanPivot) + equalToPivot + quickSortDistance(greaterThanPivot)