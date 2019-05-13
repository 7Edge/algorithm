#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: 03.insert_sort
# Date: 5/12/2019
import random


def insert_sort(li):
    """
    思路：从无序区第一个插入到有序区，主要是有序去的变化。
    有两种判断插入区域方式：
    因为循环次数固定（通过break）则需要判定跳出循环；另一种方式时：时指针方式，只要指针对应的值大
    :param li:
    :return:
    """

    for i in range(1, len(li)):  # 从1开始是因为第一个躺直接放入有序区
        # 方式一：
        # tmp = li[i]
        # for j in range(i):
        #     k = i - j - 1
        #     if tmp < li[k]:
        #         li[k], li[k + 1] = li[k + 1], li[k]
        #     else:
        #         break
        # 方式二：
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


list01 = list(range(10))
random.shuffle(list01)
print(list01)
insert_sort(list01)
print(list01)

if __name__ == '__main__':
    pass
