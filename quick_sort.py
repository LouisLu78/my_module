# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/4/26
# Email: gq4350lu@hotmail.com

def quick_sort(originalList):
    if len(originalList) <= 1:
        return originalList
    else:
        mid = originalList[len(originalList) // 2]
        originalList.remove(mid)
        left = [num for num in originalList if num < mid]
        right = [num for num in originalList if num >= mid]

        return quick_sort(left) + [mid] + quick_sort(right)


def _verify():
    list_a = [5, 3, 7, 6, 4, 1, 0, 2, 9, 10, 8]
    quick_sort(list_a)
    print(list_a)


if __name__ == '__main__':
    _verify()
