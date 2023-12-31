import random

def checkForTemp(list):
    for i in range(len(list) - 1):
        if list[i].temperature > list[i + 1].temperature:
            return False

    return True

# Bogo sort algorithm works by randomly shuffling the list until it is sorted.
def checkForDistance(list):
    for i in range(len(list) - 1):
        if list[i].distance > list[i + 1].distance:
            return False

    return True

def bogoSortTemp(list):
    returnList = list[:]

    while(checkForTemp(returnList) == False):
        random.shuffle(returnList)

    return returnList


def bogoSortDistance(list):
    returnList = list[:]

    while(checkForDistance(returnList) == False):
        random.shuffle(returnList)

    return returnList
