# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-21 21:42
# @Author  : yanlei
# @FileName: two_hundred_twenty_one.py

题目求解方法：dp
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        # row
        for i in range(len(matrix)):
            # col
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        if dp[i-1][j] >=1 and dp[i][j-1] >=1 and dp[i-1][j-1] >=1:
                            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1
                        else:
                            dp[i][j] = 1
            res = max(res, max(dp[i]))
        # print(res, dp)
        return res*res




Solution().maximalSquare([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])