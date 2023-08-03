
# the built in sorting algorithm in python utilizes timsort which is why this is a viable implementation
def timSortTemp(list):
    list.sort(key=lambda x: x.temperature)
    return list

def timSortDist(list):
    list.sort(key=lambda x: x.distance)
    return list