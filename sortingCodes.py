# merge sort algorithm code snippet
mergeSort = '''def merge(list, start, mid, end):
  left = list[start:mid + 1]
  right = list[mid + 1:end + 1]
  i = 0
  j = 0
  k = start

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
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

def mergeSort(list, start, end):
  if start < end:
    mid = start + (end - start) // 2
    mergeSort(list, start, mid)
    mergeSort(list, mid+1, end)
    merge(list, start, mid, end)'''

# selection sort algorithm code snippet
selectionSort = '''def selectionSort(list):
    for i in range(len(list)):
        minIndx = i
        for j in range(i+1, len(list)):
            if list[j] < list[minIndx]:
                minIndx = j
        list[i] = list[minIndx]
        list[minIndx] = list[i]

    return list'''