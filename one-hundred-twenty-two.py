class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pricesSub =[]
        sum = 0
        for i in range(len(prices)-1):
            pricesSub.append(prices[i+1] - prices[i])
        for item in pricesSub:
            if item > 0:
                sum = sum +item
        return sum
