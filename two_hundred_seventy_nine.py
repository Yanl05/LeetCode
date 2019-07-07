# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-07 23:33
# @Author  : yanlei
# @FileName: two_hundred_seventy_nine.py

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares

"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n for _ in range(n+1)]
        dp[0] = 0
        for i in range(n):
            j = 1
            while i+j*j<=n:
                dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
                j += 1
        return dp[-1]


print(Solution().numSquares(12))