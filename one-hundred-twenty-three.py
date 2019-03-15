class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lenp = len(prices)
        if lenp == 0 or lenp == 1 or not prices:
            return 0
        left = lenp * [0]
        right = lenp * [0]
        min = prices[0]
        for i in range(1, lenp):
            if min < prices[i]:
                left[i] = max(left[i-1], prices[i]-min)
            else:
                left[i] = left[i-1]
                min = prices[i]

        maxp = prices[lenp-1]
        for i in range(lenp-2, -1, -1):
            if maxp > prices[i]:
                right[i] = max(right[i+1], maxp-prices[i])
            else:
                right[i] = right[i+1]
                maxp = prices[i]
        print(left,'\n', right)
        result = 0
        for i in range(lenp):
            result = max(result, left[i]+right[i])
        return result







print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))