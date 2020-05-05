# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/5/2
# Email: gq4350lu@hotmail.com

import time, random


def shell_sort(originalList):
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
        print(subList)
    print()


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    shell_sort(list_a)
    printf(list_a)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    shell_sort(list_b)
    printf(list_b)

    list_c = [random.randint(1, 100000) for i in range(100000)]
    shell_sort(list_c)
    printf(list_c)


if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))
