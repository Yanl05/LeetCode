class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # pd = []
        # for i in range(len(prices) - 1):
        #     pd.append(prices[i + 1] - prices[i])
        # max = -(2**31)
        # sum = 0
        # for i in range(len(pd)):
        #     if sum <= 0:
        #         sum = pd[i]
        #     else:
        #         sum = sum + pd[i]
        #     if max < sum:
        #         max = sum
        # if max <= 0:
        #     return 0
        # else:
        #     return max

        # 36ms 36%
        # if not prices:
        #     return 0
        # pd = [0] * len(prices)
        # sale = 0
        # for index, num in enumerate(prices):
        #     if index == 0:
        #         buy = num
        #     else:
        #         if num > buy:
        #             sale = max(sale, num)
        #             pd[index] = max((sale - buy), pd[index-1])
        #         else:
        #             buy = num
        #             sale = 0
        #             pd[index] = pd[index-1]
        # return pd


        # 100%
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif (price - min_price) > max_profit:
                max_profit = price - min_price
        return max_profit

print(Solution().maxProfit([3,2,6,5,0,3]))