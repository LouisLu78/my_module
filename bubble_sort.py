# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/6
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

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
        print(orignal_list)
        flag = 1
    return orignal_list


def _verify():
    list_a = [2, 6, 4, 8, 10, 12, 89, 68, 45, 37, 43, 5.14, 456, 84]
    bubble_sort(list_a)


if __name__ == "__main__":
    _verify()
