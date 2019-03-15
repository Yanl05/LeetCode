class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        iCurrentMax = 0
        dp = [0]
        iFinalMax = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                dp.append(prices[i + 1] - prices[i])
            else:
                dp.append(0)
        print(dp)
        dp2=[]
        tmp=0
        for index, i in enumerate(dp):
            if i == 0:
                if tmp != 0:
                    dp2.append(tmp)

                tmp = 0
                continue
            else:
                tmp+=i
                if index == len(dp)-1:
                    dp2.append(tmp)
            dp2.sort()
            dp2.reverse()
            print(dp2)
            ret = 0
            for i in range(k):
                ret += dp2[i]


        print(dp2, ret)




# print(Solution().maxProfit(2,[3,2,6,5,0,3]))
print(Solution().maxProfit(2,[1,2,3,4,5]))