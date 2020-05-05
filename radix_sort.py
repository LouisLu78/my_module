# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/5/5
# Email: gq4350lu@hotmail.com

import time, random
import math


def radix_sort(originalList):
    size = len(originalList)
    k = 0
    radix = 1
    number = max(originalList)
    digit = int(math.log(number, 10)) + 1
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


def printf(originalList):
    for i in range(0, len(originalList), 20):
        subList = list(originalList[i:i + 20])
        print(subList)
    print()


def _verify():
    list_b = [2, 615, 4, 8123, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    radix_sort(list_b)
    printf(list_b)

    list_c = [random.randint(1, 100000) for i in range(100000)]
    radix_sort(list_c)
    printf(list_c)


if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))
