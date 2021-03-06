# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/4/28
# Email: gq4350lu@hotmail.com

import time, random

def insert_sort(original_list):
    size = len(original_list)
    for i in range(size - 1):
        temp = original_list[i + 1]
        for j in range(i, -1, -1):
            if original_list[j] > temp:
                original_list[j + 1] = original_list[j];
                original_list[j] = temp;
            else:
                break

    return original_list


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    insert_sort(list_a)
    print(list_a)

    list_b = [2, 6, 4, 8, 10, 12, 89, 68, 3.14, 45, 37, 43, 456, 84]
    insert_sort(list_b)
    print(list_b)

    list_c = [random.randint(1, 100000) for i in range(100000)]
    l = insert_sort(list_c)
    print(l)

if __name__ == '__main__':
    start = time.time()
    _verify()
    end = time.time()
    print("The sorting program costs %.2f seconds." % (end - start))
