# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/5/7
# Email: gq4350lu@hotmail.com

import time, random
import math

def bubbleSort(originalList):
    size = len(originalList)
    flag = 1
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if originalList[j] > originalList[j + 1]:
                originalList[j], originalList[j + 1] = originalList[j + 1], originalList[j]
                flag = 0
        if flag:
            break
        flag = 1


class HeapSort:
    def __init__(self, originalList):
        self.originalList = originalList
        self.sort()

    def buildHeap(self):
        length = len(self.originalList)
        for i in range(length // 2 - 1, -1, -1):
            HeapSort.adjustHeap(self.originalList, i, length)

    @staticmethod
    def adjustHeap(aList, index, length):

        temp = aList[index]
        left = 2 * index + 1
        while left < length:
            if left + 1 < length and aList[left] < aList[left + 1]:
                left += 1
            if aList[index] < aList[left]:
                aList[index] = aList[left]
                index = left
                left = 2 * index + 1
            else:
                break
            aList[index] = temp

    def sort(self):
        self.buildHeap()

        length = len(self.originalList)
        for i in range(length - 1, -1, -1):
            self.originalList[0], self.originalList[i] = self.originalList[i], self.originalList[0]
            HeapSort.adjustHeap(self.originalList, 0, i)

    def __str__(self):
        s = ""
        for i in range(len(self.originalList)):
            s += str(self.originalList[i]) + " "
            if i % 20 == 19:
                s += "\n"
        return s


def insertSort(original_list):
    size = len(original_list)
    for i in range(size - 1):
        temp = original_list[i + 1]
        for j in range(i, -1, -1):
            if original_list[j] > temp:
                original_list[j + 1] = original_list[j];
                original_list[j] = temp;
            else:
                break


class MergeSort:
    def __init__(self, originalList):
        self.originalList = originalList
        self.sort()

    @staticmethod
    def merge(unsortedList, first, mid, last, sortedList):
        k = 0
        i = first
        j = mid
        while i < mid and j < last:
            if unsortedList[i] < unsortedList[j]:
                sortedList[k] = unsortedList[i]
                i += 1
            else:
                sortedList[k] = unsortedList[j]
                j += 1
            k += 1
        while i < mid:
            sortedList[k] = unsortedList[i]
            i += 1
            k += 1

        for m in range(k):
            unsortedList[first + m] = sortedList[m]

    def mergeSort(self, first, last, sortedList):
        mid = (first + last) // 2
        if first < last - 1:
            self.mergeSort(first, mid, sortedList)
            self.mergeSort(mid, last, sortedList)
            MergeSort.merge(self.originalList, first, mid, last, sortedList)

    def sort(self):
        size = len(self.originalList)
        sortedList = [0] * size
        self.mergeSort(0, size, sortedList)

    def __str__(self):
        s = ""
        for i in range(len(self.originalList)):
            s += str(self.originalList[i]) + " "
            if i % 20 == 19:
                s += "\n"
        return s


def quickSort(originalList):
    if len(originalList) <= 1:
        return originalList
    else:
        mid = originalList[len(originalList) // 2]
        originalList.remove(mid)
        left = [num for num in originalList if num < mid]
        right = [num for num in originalList if num >= mid]

        originalList = quickSort(left) + [mid] + quickSort(right)
        return originalList


def radixSort(originalList):
    number = max(originalList)
    digit = int(math.log(number, 10)) + 1

    k, radix = 0, 1
    sortedList = [[] for i in range(10)]

    for i in range(digit):
        for j in originalList:
            m = int(j / radix) % 10
            sortedList[m].append(j)
        for subList in sortedList:
            for num in subList:
                originalList[k] = num
                k += 1
        k = 0
        radix *= 10
        sortedList = [[] for i in range(10)]


def selectSort(originalList):
    size = len(originalList)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if originalList[i] > originalList[j]:
                originalList[i], originalList[j] = originalList[j], originalList[i]


def shellSort(originalList):
    size = len(originalList)
    d = size // 2

    while (d > 0):
        for i in range(d):
            for j in range(i, size - d, d):
                temp = originalList[j + d]
                for k in range(j, -1, -d):
                    if originalList[k] > temp:
                        originalList[k + d] = originalList[k]
                        originalList[k] = temp
                    else:
                        break
        d = d // 2


def printf(originalList):
    for i in range(0, len(originalList), 20):
        subList = list(originalList[i:i + 20])
        for num in subList:
            print("%6d" % num, end = "")
        print()
    print()


def _main():
    start = time.time()

    aList = [random.randint(1, 10000) for i in range(10000)]
    bubbleSort(aList)
    printf(aList)
    endBubble = time.time()
    print("The bubble-sorting program for 1E4 numbers costs %.2f seconds." % (endBubble - start))

    aList = [random.randint(1, 100000) for i in range(100000)]
    hs = HeapSort(aList)
    print(hs)
    endHeap = time.time()
    print("The heap-sorting program for 1E5 numbers costs %.2f seconds." % (endHeap - endBubble))

    aList = [random.randint(1, 10000) for i in range(10000)]
    insertSort(aList)
    printf(aList)
    endInsert = time.time()
    print("The insert-sorting program for 1E4 numbers costs %.2f seconds." % (endInsert - endHeap))

    aList = [random.randint(1, 100000) for i in range(100000)]
    ms = MergeSort(aList)
    print(ms)
    endMerge = time.time()
    print("The merge-sorting program for 1E5 numbers costs %.2f seconds." % (endMerge - endInsert))

    aList = [random.randint(1, 100000) for i in range(100000)]
    l = quickSort(aList)
    printf(l)
    endQuick = time.time()
    print("The quick-sorting program for 1E5 numbers costs %.2f seconds." % (endQuick - endMerge))

    aList = [random.randint(1, 100000) for i in range(100000)]
    radixSort(aList)
    printf(aList)
    endRadix = time.time()
    print("The radix-sorting program for 1E5 numbers costs %.2f seconds." % (endRadix - endQuick))

    aList = [random.randint(1, 10000) for i in range(10000)]
    selectSort(aList)
    printf(aList)
    endSelect = time.time()
    print("The select-sorting program for 1E4 numbers costs %.2f seconds." % (endSelect - endRadix))

    aList = [random.randint(1, 100000) for i in range(100000)]
    shellSort(aList)
    printf(aList)
    endShell = time.time()
    print("The shell-sorting program for 1E5 numbers costs %.2f seconds." % (endShell - endSelect))

if __name__ == "__main__":
    _main()