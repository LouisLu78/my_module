# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/4/28
# Email: gq4350lu@hotmail.com

import time, random

def select_sort(originalList):
    size = len(originalList)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if originalList[i] > originalList[j]:
                originalList[i], originalList[j] = originalList[j], originalList[i]

    return originalList


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    select_sort(list_a)
    print(list_a)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    select_sort(list_b)
    print(list_b)

    list_c = [random.randint(1, 10000) for i in range(10000)]
    l = select_sort(list_c)
    print(l)


if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))


