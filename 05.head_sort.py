#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: 05 head_sort
# Date: 5/13/2019
"""
关于堆排序：
首先，将列表看作一个 完全二叉树；
然后，将完全二叉树 转换为 大根堆
接着，取出大根堆的最大放入列表，将后叶节点放到最大位置，进行堆的向下调整。
最后，将堆调整完成后，重复第三步。
pythoy列表默认排序是堆排序，只不过是
"""
import heapq
import random

list01 = list(range(50))
random.shuffle(list01)
print(list01)

# 先将
heapq.heapify(list01)  # 将list01 变为一个小根堆
# 从小根堆中取值最小值
print(heapq.heappop(list01))
print(heapq.heappop(list01))
print(heapq.heappop(list01))
print(heapq.heappop(list01))
# 像小根堆中再放入一个值，重新构成一个小根堆
heapq.heappush(list01, 0)
print(heapq.heappop(list01))




if __name__ == '__main__':
    pass
