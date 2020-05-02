# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/5/2
# Email: gq4350lu@hotmail.com

import time, random
from insert_sort import *

def shell_sort(originalList):
    size = len(originalList)
    d = size // 2
    newList = []
    while(d > 0):
        for i in range(d):
            subList = [originalList[j] for j in range(i, size, d)]
            insert_sort(subList)
            newList += subList
        originalList = newList
        newList = []
        d = d // 2

    return originalList

def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]

    l = shell_sort(list_a)
    print(l)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    l = shell_sort(list_b)
    print(l)

    list_c =[]
    for i in range(10000):
        list_c.append(random.randint(1, 10000))
    l = shell_sort(list_c)
    print(l)

if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds."%(end - start))
