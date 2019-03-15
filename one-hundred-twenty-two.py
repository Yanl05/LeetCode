class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # pricesSub =[]
        # sum = 0
        # for i in range(len(prices)-1):
        #     pricesSub.append(prices[i+1] - prices[i])
        # for item in pricesSub:
        #     if item > 0:
        #         sum = sum +item
        # return sum

        # 16%
        # dp = [0] * len(prices)
        # buy = float('inf')
        # sale = 0
        # for i in range(len(prices)):
        #     if i == 0:
        #         buy = prices[i]
        #     else:
        #         if prices[i] < sale:
        #             dp[i-1] = sale - buy + dp[i-2]
        #             buy = prices[i]
        #             sale = 0
        #             dp[i] = dp[i-1]
        #         elif prices[i] < buy and sale == 0:
        #             buy = prices[i]
        #             dp[i] = dp[i - 1]
        #         elif prices[i] > buy and i != len(prices)-1:
        #             sale = prices[i]
        #             dp[i] = dp[i-1]
        #         else:
        #             sale = prices[i]
        #             dp[i] = sale - buy + dp[i-1]
        #
        # return dp[-1]


        # 100%
        iCurrentMax = 0
        iFinalMax = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                iCurrentMax += prices[i+1] - prices[i]
        return iCurrentMax










print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
# print(Solution().maxProfit([7,1,5,3,6,4]))
