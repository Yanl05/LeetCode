# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-05 10:23
# @Author  : yanlei
# @FileName: 买卖股票的最佳时机二.py

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp数组，空间复杂度 o(n)
        # if not prices:
        #     return 0
        # # 1.状态
        # dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        # # 2.base case
        # # 3.状态转移方程
        # for i in range(len(prices)):
        #     if i - 1 == -1:
        #         dp[i][0] = 0
        #         #  dp[0][1]
        #         #  = max(dp[-1][1], dp[-1][0] - prices[i])
        #         #   = max(-infinity, 0 - prices[i])
        #         # = -prices[i]
        #
        #         dp[i][1] = -prices[i]
        #         continue
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        #
        # return dp[-1][0]

        # dp 空间复杂度 o(1)
        # 初始状态
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        # 状态转移方程
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
