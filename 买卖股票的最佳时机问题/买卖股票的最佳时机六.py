# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-05 23:04
# @Author  : yanlei
# @FileName: 买卖股票的最佳时机六.py

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # 初始状态
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        # 状态转移方程
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i]-fee)
            dp_i_1 = max(dp_i_1, tmp-prices[i])
        return dp_i_0





print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
