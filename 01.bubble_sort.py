#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: bubble_sort
# Date: 5/12/2019


def bubble_sort(li):
    """
    1. 每一次冒泡遍历的时无序区0：len(无序区-1)
    2. 冒泡的躺数时列表长度-1，而每趟的冒泡无序区长度时 列表长度-有序区长度，其实就是列表长度 - 第几躺
    3. 最后在冒泡遍历时，遇到大的就交换。
    4. 优化：一趟冒泡如果没有出现交换，那么下次就不要在冒泡了，因为无序区其实已经有序了。
    关键词： 随着有序区指针变化而冒泡
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


li01 = [1, 3, 4, 3, 5, 6, 7, 3, 2, 5, 7, 4, 6, 7]

bubble_sort(li01)

print(li01)

if __name__ == '__main__':
    pass
