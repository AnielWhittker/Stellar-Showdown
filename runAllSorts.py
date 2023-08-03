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
import bitonicSort as bitSort

def runAllSorts(list, sortBy):
    returnDict = {}

    if sortBy == "temp":

        start = time.time()
        ms.mergeSortTemperature(list, 0, len(list) - 1)
        end = time.time()

        returnDict["Merge Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ss.selectionSortTemp(list)
        end = time.time()

        returnDict["Selection Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bsort.bubbleSortTemp(list)
        end = time.time()

        returnDict["Bubble Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        shs.shellSortTemp(list)
        end = time.time()

        returnDict["Shell Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        qs.quickSortTemp(list)
        end = time.time()

        returnDict["Quick Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ts.timSortTemp(list)
        end = time.time()

        returnDict["Tim Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        hs.heapSortTemp(list)
        end = time.time()

        returnDict["Heap Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bitSort.bitonicSortTemp(list)
        end = time.time()

        returnDict["Bitonic Sort"] = str("{:.4f}".format(end - start))


    elif sortBy == "distance":

        start = time.time()
        ms.mergeSortDistance(list, 0, len(list) - 1)
        end = time.time()

        returnDict["Merge Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ss.selectionSortDist(list)
        end = time.time()

        returnDict["Selection Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bsort.bubbleSortDist(list)
        end = time.time()

        returnDict["Bubble Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        shs.shellSortDistance(list)
        end = time.time()

        returnDict["Shell Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        qs.quickSortDistance(list)
        end = time.time()

        returnDict["Quick Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        ts.timSortDist(list)
        end = time.time()

        returnDict["Tim Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        hs.heapSortDist(list)
        end = time.time()

        returnDict["Heap Sort"] = str("{:.4f}".format(end - start))



        start = time.time()
        bitSort.bitonicSortDist(list)
        end = time.time()

        returnDict["Bitonic Sort"] = str("{:.4f}".format(end - start))


    returnDict["Bogo Sort"] = "N/A"


    return returnDict



