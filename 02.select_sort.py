#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: select_sort
# Date: 5/12/2019
import random


def select_sort(li):
    """
    思路： 从无序区选择一个最小的与无序区的第一个交换，这时候无序区的开始索引+1，有序区则多了一个。主要就是每次躺找最小，然后缩小
    无序区，无需关心有序去的变化。
    关键词：选最小，无序区指针随着遍历变化。
    1. 躺数 len(li) -1 ，
    2. 用一个变量存储 无序区最小的索引
    3. 每趟无序区的区间时i: len(li)
    4. 找到最小的后与第一个交换，将第一个变为到有序去去。

    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


l = list(range(500))
print(l)
random.shuffle(l)
print(l)
select_sort(l)
print(l)

if __name__ == '__main__':
    pass
