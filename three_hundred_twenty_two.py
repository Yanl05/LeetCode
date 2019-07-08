# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-08 18:32
# @Author  : yanlei
# @FileName: three_hundred_twenty_two.py

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for j in coins:
                if i-j>=0 and dp[i-j] != float('inf'):
                    dp[i] = dp[i-j]+1
                    print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1


print(Solution().coinChange([1, 5], 11))