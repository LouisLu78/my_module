# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/5/3
# Email: gq4350lu@hotmail.com

import time, random


class Heap_sort():
    def __init__(self, originalList):
        self.originalList = originalList
        self.sort()

    def buildHeap(self):
        length = len(self.originalList)
        for i in range(length // 2 - 1, -1, -1):
            self.adjustHeap(i, length)

    def adjustHeap(self, index, length):

        temp = self.originalList[index]
        left = 2 * index + 1
        while left < length:
            if left + 1 < length and self.originalList[left] < self.originalList[left + 1]:
                left += 1
            if self.originalList[index] < self.originalList[left]:
                self.originalList[index] = self.originalList[left]
                index = left
                left = 2 * index + 1
            else:
                break
            self.originalList[index] = temp

    def sort(self):
        self.buildHeap()

        length = len(self.originalList)
        for i in range(length - 1, -1, -1):
            self.originalList[0], self.originalList[i] = self.originalList[i], self.originalList[0]
            self.adjustHeap(0, i)

    def __str__(self):
        s = ""
        for i in range(len(self.originalList)):
            s += str(self.originalList[i]) + " "
            if i % 20 == 19:
                s += "\n"
        return s


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    hsa = Heap_sort(list_a)
    print(hsa)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    hsb = Heap_sort(list_b)
    print(hsb)

    list_c = [random.randint(1, 100000) for i in range(100000)]
    hsc = Heap_sort(list_c)
    print(hsc)


if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))
