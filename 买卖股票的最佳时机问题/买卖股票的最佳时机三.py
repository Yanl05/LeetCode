# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-05 21:55
# @Author  : yanlei
# @FileName: 买卖股票的最佳时机三.py


给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # 1. 状态  最多买卖两次  则 为 k=3
        # dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        # for i in range(len(prices)):
        #     for k in range(1,3):
        #         # 2. 初始状态
        #         if i == 0:
        #             dp[i][k][0] = 0
        #             dp[i][k][1] = -prices[0]
        #             continue
        #         # 3. 状态转移方程
        #         dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
        #         dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        #
        # print(dp)
        # return dp[-1][2][0]

        # 1. 初始状态 dp为当前最大利润
        dp_i_1_0, dp_i_2_0 = 0, 0
        dp_i_1_1, dp_i_2_1 = float('-inf'), float('-inf')
        # 2. 状态转移方程
        for i in range(len(prices)):
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1+prices[i])
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0-prices[i])
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1+prices[i])
            dp_i_1_1 = max(dp_i_1_1, -prices[i])
        return dp_i_2_0











print(Solution().maxProfit([3,3,5,0,0,3,1,4]))