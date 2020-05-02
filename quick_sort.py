# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/4/26
# Email: gq4350lu@hotmail.com

import time, random

def quick_sort(originalList):
    if len(originalList) <= 1:
        return originalList
    else:
        mid = originalList[len(originalList) // 2]
        originalList.remove(mid)
        left = [num for num in originalList if num < mid]
        right = [num for num in originalList if num >= mid]

        originalList = quick_sort(left) + [mid] + quick_sort(right)
        return originalList


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    l = quick_sort(list_a)
    print(l)
    print(list_a)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    l = quick_sort(list_b)
    print(l)

    list_c =[]
    for i in range(100000):
        list_c.append(random.randint(1, 100000))
    l = quick_sort(list_c)
    print(l)

if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds."%(end - start))
