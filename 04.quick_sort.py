#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: quick_sort
# Date: 5/13/2019
import random


def quick_sort(li):
    """
    思路：快速排序有两个指针left，right和一个mid值；一趟操作是，一次left一次right，当左边

    1. 找到mid的值，用于左右比较

    关键词： 取第一个位切片值(这个位置就可以作为交换的存储位置)，切片位置，交换，递归;对于切片位置，一循环嵌套两循环，两循环都是为了找到符合条件的位置，找到后马上和
           另一边交换，另一边则因为刚交换的肯定是符合的，所以继续循环。直到两个循环都进不去，说明左右重合，这时候两个都进不去，外层也
           跳出，这时候左右相等的位置就赋值为tmp值。也得到了中间位置，利用嵌套再次排序左右子列表。
    :param li:
    :return:
    """

    def _quick_sort(li_inner, left, right):
        if left < right:  # 这个是递归得结束条件，当只有一个得时候
            mid = partition(li_inner, left, right)
            # 先递归左边排序
            _quick_sort(li_inner, left, mid - 1)
            # 再递归右边排序
            _quick_sort(li_inner, mid + 1, right)

    _quick_sort(li, 0, len(li) - 1)


def partition(li, left, right):  # 先进行一次分片，得到分片的中间位置
    tmp = li[left]

    # 交换循环：停止的条件是left>=right,这时候就得到了tmp应该放置的位置，然后将tmp放入
    while left < right:
        # 由于已经从left左边取出了一个，所以先从右边开始；并且为了避免特殊情况，就是右边已经找完，越过中间到小的区域，所以left<right
        # 还是要加上
        while left < right and li[right] >= tmp:  # 如果要降序排序只需要将 >= 换成<=;下一个循环得也转换。
            right -= 1  # 一种right指针，进行右边的下一个判定
        # 如果右边循环跳出，说明已经找到了一个小于temp的值，这时候和左边进行交换，对于第一次，交换的是中间值，中间值将在下面的做循环后换回一个
        # 数据右边的大值。
        li[left] = li[right]
        # 进行左边循环的找大于tmp的值，然后交换。
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
        # 如果left < right 还成立，那么继续交换
    # 最后交换完成，left == right ，得到了tmp应该放置的位置，也就是切片值得位置
    li[left] = tmp

    return left


if __name__ == '__main__':
    l = list(range(500))
    print(l)
    random.shuffle(l)
    print(l)
    quick_sort(l)
    print(l)
