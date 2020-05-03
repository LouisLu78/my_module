# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/6
# Email: gq4350lu@hotmail.com

import time, random


def bubble_sort(orignal_list):
    size = len(orignal_list)
    flag = 1
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if orignal_list[j] > orignal_list[j + 1]:
                orignal_list[j], orignal_list[j + 1] = orignal_list[j + 1], orignal_list[j]
                flag = 0
        if flag:
            break
        flag = 1
    return orignal_list


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    l = bubble_sort(list_a)
    print(l)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    l = bubble_sort(list_b)
    print(l)

    list_c = [random.randint(1, 10000) for i in range(10000)]
    l = bubble_sort(list_c)
    print(l)


if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))
