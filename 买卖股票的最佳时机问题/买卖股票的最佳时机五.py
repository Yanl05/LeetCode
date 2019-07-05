# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-05 21:12
# @Author  : yanlei
# @FileName: 买卖股票的最佳时机五.py

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp数组 空间复杂度 o(n)
        # if not prices:
        #     return 0
        # n = len(prices)
        # # 1. 状态
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # for i in range(n):
        #     # 2. base case
        #     if i == 0:
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[0]
        #         continue
        #     # 3. 状态转移方程
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        # return dp[-1][0]

        # dp 空间复杂度 o(1)
        if not prices:
            return 0
        # 1. 状态
        # 2. base case
        dp_i_0 = 0
        dp_i_1 = -prices[0]
        # 保存两天前的dp_i_0的值
        dp_pre_0 = 0
        # 3. 状态转移方程
        for i in range(len(prices)):
            # 一天前的 dp_i_0
            tmp = dp_i_0
            # 跟新了一次dp_i_0  该值变为1天前的dp_i_0  .tmp则变成两天前的dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,dp_pre_0-prices[i])
            # 将新的两天前的值 重新赋值为dp_pre_0
            dp_pre_0 = tmp
        return dp_i_0









print(Solution().maxProfit([1,2,3,0,2]))
# print(Solution().maxProfit([3,3,5,0,0,3,1,4]))