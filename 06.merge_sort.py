#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: 06. guibing_sort
# Date: 5/13/2019
"""
归并排序
"""
import random
import sys

sys.setrecursionlimit(100000)


def merge_sort(li, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(li, left, mid)
        merge_sort(li, mid + 1, right)
        merging(li, left, mid, right)


def merging(li, left, mid, right):
    """
    归并排序，首先完成一次归并，
    一次归并得思路：li1和li2都是有序列表，创建一个合并后得列表。然后两个列表指针进行移动，最初是比较最小得，如果谁小，谁放入列表，然后，
    移动指针，大得不动。最后当任意一个指针先完，那么列一个列表直接放入到列表中。

    关键字：两个列表指针，还没遍历完成单独进行遍历加入到新列表中
    """
    tmp_list = list()
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if li[i] <= li[j]:
            tmp_list.append(li[i])
            i += 1
        else:
            tmp_list.append(li[j])
            j += 1
    while i <= mid:
        tmp_list.append(li[i])
        i += 1
    while j <= right:
        tmp_list.append(li[j])
        j += 1
    li[left:right + 1] = tmp_list


if __name__ == '__main__':
    # 一次归并测试
    list01 = [2, 4, 5, 8, 9, 1, 4, 7, 9]
    print(list01)
    merging(list01, 0, 4, 8)
    print(list01)
    # 归并测试
    list02 = list(range(50))
    print(list02)
    random.shuffle(list02)
    print(list02)
    merge_sort(list02, 0, len(list02) - 1)
    print(list02)
