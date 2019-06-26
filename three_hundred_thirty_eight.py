# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-26 20:27
# @Author  : yanlei
# @FileName: three_hundred_thirty_eight.py

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]

题解；
数分为两类：  奇书
                奇书比前一个偶数多一个 1

            偶数
                偶数中的 1 和 该数 /2 之后的 1 个数一样多
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret_list = []
        for i in range(num+1):
            if i == 0:
                ret_list.append(0)
                continue
            if i%2!=0: # 奇数
                ret_list.append(ret_list[i-1]+1)
            else:
                ret_list.append(ret_list[int(i/2)])
                # print(i/2)
        return ret_list


print(Solution().countBits(99))