class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pd = []
        for i in range(len(prices) - 1):
            pd.append(prices[i + 1] - prices[i])
        max = -(2**31)
        sum = 0
        for i in range(len(pd)):
            if sum <= 0:
                sum = pd[i]
            else:
                sum = sum + pd[i]
            if max < sum:
                max = sum
        if max <= 0:
            return 0
        else:
            return max
        
