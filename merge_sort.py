# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/5/4
# Email: gq4350lu@hotmail.com

import time, random


class Merge_sort:
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
        if first + 1 < last:
            self.mergeSort(first, mid, sortedList)
            self.mergeSort(mid, last, sortedList)
            Merge_sort.merge(self.originalList, first, mid, last, sortedList)

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


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    msa = Merge_sort(list_a)
    print(msa)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    msb = Merge_sort(list_b)
    print(msb)

    list_c = [random.randint(1, 100000) for i in range(100000)]
    msc = Merge_sort(list_c)
    print(msc)


if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))
