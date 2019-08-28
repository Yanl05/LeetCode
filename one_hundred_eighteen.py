# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-28 16:33
# @Author  : yanlei
# @FileName: one_hundred_eighteen.py

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows == 0: return ret
        for i in range(numRows):
            ret.append([1]*(i+1))
            if i > 1:
                for j in range(1,i):
                    ret[-1][j] = ret[-2][j-1] + ret[-2][j]
        return ret




print(Solution().generate(5))