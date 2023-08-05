import streamlit as st
import time
import mergeSort as ms
import selectionSort as ss
import bubbleSort as bsort
import shellSort as shs
import timSort as ts
import quickSort as qs
import heapSort as hs
import bogoSort as bogo
import insertionSort as inssort
import bitonicSort as bitSort

# runAllSorts.py contains the code for running all the sorting algorithms on the list of stars.
def runAllSorts(list, sortBy):
    returnDict = {}

    temp = list[:]

    if sortBy == "temp":

        start = time.time()
        ms.mergeSortTemperature(temp, 0, len(list) - 1)
        end = time.time()

        temp = list[:]

        returnDict["Merge Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ss.selectionSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Selection Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bsort.bubbleSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Bubble Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        shs.shellSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Shell Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        qs.quickSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Quick Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ts.timSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Tim Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        hs.heapSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Heap Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bitSort.bitonicSortTemp(temp, 0, len(temp), 1)
        end = time.time()

        temp = list[:]

        returnDict["Bitonic Sort"] = str("{:.4f}".format(end - start))

        start = time.time()
        inssort.insertionSortTemp(temp)
        end = time.time()

        temp = list[:]

        returnDict["Insertion Sort"] = str("{:.4f}".format(end - start))


    elif sortBy == "distance":

        start = time.time()
        ms.mergeSortDistance(temp, 0, len(list) - 1)
        end = time.time()

        temp = list[:]

        returnDict["Merge Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ss.selectionSortDist(temp)
        end = time.time()

        temp = list[:]

        returnDict["Selection Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bsort.bubbleSortDist(temp)
        end = time.time()

        temp = list[:]

        returnDict["Bubble Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        shs.shellSortDistance(temp)
        end = time.time()

        temp = list[:]

        returnDict["Shell Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        qs.quickSortDistance(temp)
        end = time.time()

        temp = list[:]

        returnDict["Quick Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ts.timSortDist(temp)
        end = time.time()

        temp = list[:]

        returnDict["Tim Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        hs.heapSortDist(temp)
        end = time.time()

        temp = list[:]

        returnDict["Heap Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bitSort.bitonicSortDist(temp, 0, len(list), 1)
        end = time.time()

        returnDict["Bitonic Sort"] = str("{:.4f}".format(end - start))

        start = time.time()
        inssort.insertionSortDist(temp)
        end = time.time()

        temp = list[:]

        returnDict["Insertion Sort"] = str("{:.4f}".format(end - start))


    returnDict["Bogo Sort"] = "N/A"


    return returnDict



