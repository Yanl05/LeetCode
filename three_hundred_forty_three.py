# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-04 10:13
# @Author  : yanlei
# @FileName: three_hundred_forty_three.py
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i - 1, 1, -1):
                # dp        原数    拆分后的maxdp[i]*j  未拆分的i*j
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
            print(dp)
        return dp[-1]


print(Solution().integerBreak(10))
