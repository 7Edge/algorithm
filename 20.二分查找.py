#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: 20.二分查找
# Date: 5/21/2019
"""
二分查找：在大小顺序排列好的序列中查找出想要的值的，通常就是使用二分查找法。
前提条件：有序序列，升序还是降序
二分思路：将要被查找的序列分为两部分，判断查找的目标值在大的部分还是小的部分，然后再将所在的部分再次进行二分，判断目标值所属部分。。。再
        进行分，最后还剩一个的时候，就是不能再分的时候，判定值是否相等，如果不等，那么目标值不在其中，如果相等则可以找到，并且得到索引。
适用场景：适用于不经常变动而查找频繁的有序列表。
"""


# 循环二分
def binary_search(data_sort_list, to_find_val):
    low = 0
    high = len(data_sort_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = data_sort_list[mid]
        if guess > to_find_val:
            high = mid - 1
        elif guess < to_find_val:
            low = mid + 1
        else:
            return mid
    return None


# 递归二分
def binary_search2(data, low, high, val):
    if low > high:
        return None
    mid = (low + high) // 2
    guess = data[mid]
    if guess > val:
        high = mid - 1
    elif guess < val:
        low = mid + 1
    else:
        return mid
    return binary_search2(data, low, high, val)


if __name__ == '__main__':
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
    # sorted_list = [1]
    print(binary_search(sorted_list, 7))

    print(binary_search2(sorted_list, 0, len(sorted_list)-1, 7))
