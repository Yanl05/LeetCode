# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-05 08:56
# @Author  : yanlei
# @FileName: 买卖股票的最佳时机一.py

leetcode 121 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp = [0]*len(prices)
        # for i in range(1, len(prices)):
        #     dp[i] = max(prices[i] - prices[i-1]+dp[i-1], dp[i-1])
        #
        # return dp

        # n = len(prices)
        # # 状态
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # for i in range(n):
        #     # base case
        #     if i-1 == -1:
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[i]
        #         continue
        #     # 状态转移方程
        #     # 观察状态转移方程，新状态 只与 相邻的前一状态有关。
        #     #           可以不用整个dp数组，使用一组变量即可。将空间复杂度降到 o(1)
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     dp[i][1] = max(dp[i-1][1], -prices[i])
        # return dp

        # 空间复杂度 o(1)
        n = len(prices)
        # base case
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

print(Solution().maxProfit([7,1,5,3,6,4]))
