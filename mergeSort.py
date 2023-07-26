def mergeTemperature(list, start, mid, end):
  left = list[start:mid + 1]
  right = list[mid + 1:end + 1]
  i = 0
  j = 0
  k = start

  while i < len(left) and j < len(right):
    if left[i].temperature <= right[j].temperature:
      list[k] = left[i]
      i += 1
    else:
      list[k] = right[j]
      j += 1
    k += 1

  while i < len(left):
    list[k] = left[i]
    i += 1
    k += 1

  while j < len(right):
    list[k] = right[j]
    j += 1
    k += 1

def mergeSortTemperature(list, start, end):
  if start < end:
    mid = start + (end - start) // 2
    mergeSortTemperature(list, start, mid)
    mergeSortTemperature(list, mid+1, end)
    mergeTemperature(list, start, mid, end)

def mergeDistance(list, start, mid, end):
  left = list[start:mid + 1]
  right = list[mid + 1:end + 1]
  i = 0
  j = 0
  k = start

  while i < len(left) and j < len(right):
    if left[i].distance <= right[j].distance:
      list[k] = left[i]
      i += 1
    else:
      list[k] = right[j]
      j += 1
    k += 1

  while i < len(left):
    list[k] = left[i]
    i += 1
    k += 1

  while j < len(right):
    list[k] = right[j]
    j += 1
    k += 1

def mergeSortDistance(list, start, end):
  if start < end:
    mid = start + (end - start) // 2
    mergeSortDistance(list, start, mid)
    mergeSortDistance(list, mid+1, end)
    mergeDistance(list, start, mid, end)