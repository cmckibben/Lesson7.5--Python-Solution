from random import random
import time
import csv
from itertools import zip_longest

def linearSearch(array, numToFind) -> int:
    for i in array:
        if i == numToFind: return i
    return -1

def binarySearch(array, numToFind) -> int:
    left = 0
    right = len(array) - 1
    middle = 0
    while left <= right:
        middle = int((left + right) / 2)
        if numToFind < array[middle]:
            right = middle - 1
        elif numToFind > array[middle]:
            left = middle + 1
        else:
            return middle
    return -1


if __name__ == '__main__':
    #runs = 1000
    runs = 1000000
    testarray = [1, 2, 3, 4, 5, 6, 7, 8]
    print(linearSearch(testarray, 96))
    print(binarySearch(testarray, 96))
    # No reason to change anything below this line, but feel free to browse
    print("Number of trials: " + str(runs))
    size = 100000
    # unsorted array to search
    unsortedArray = []
    for i in range(size):
        unsortedArray.append(int((random() * 99) + 1))

    sortedArray = []
    for i in range(size):
        sortedArray.append(i)
    # for timing
    linearSearchRunTimesSorted = []
    binarySearchRunTimesSorted = []
    linearSearchRunTimesUnsorted = []
    counter = 0
    average = 0

    for i in range(runs):
        startTime = time.time_ns()
        linearSearch(unsortedArray, size + 1)
        endTime = time.time_ns()
        linearSearchRunTimesUnsorted.append((endTime - startTime))

    counter = 0
    for value in linearSearchRunTimesUnsorted:
        counter += value
    average = int(counter / runs)
    print("\tLinear Search average runtime for unsorted array: " + str(average) + " nanoseconds")

    for i in range(runs):
        startTime = time.time_ns()
        linearSearch(sortedArray, size + 1)
        endTime = time.time_ns()
        linearSearchRunTimesSorted.append((endTime - startTime))

    counter = 0
    for value in linearSearchRunTimesSorted:
        counter += value
    average = int(counter / runs)
    print("\tLinear Search average runtime for sorted array:   " + str(average) + " nanoseconds")

    for i in range(runs):
        startTime = time.time_ns()
        binarySearch(sortedArray, size + 1)
        endTime = time.time_ns()
        binarySearchRunTimesSorted.append((endTime - startTime))

    counter = 0
    for value in binarySearchRunTimesSorted:
        counter += value
    average = int(counter / runs)
    print("\tBinary Search average runtime for sorted array:   " + str(average) + " nanoseconds")
    runlist = range(runs);
    data = [runlist,linearSearchRunTimesUnsorted,linearSearchRunTimesSorted,binarySearchRunTimesSorted]
    export_data = zip_longest(*data, fillvalue = '')
    with open('runtimes.csv', 'w', encoding="ISO-8859-1", newline='') as file:
          write = csv.writer(file)
          write.writerow(("Run","Python Linear Search Sorted", "Python Linear Search Unsorted","Python Binary Search Sorted"))
          write.writerows(export_data)