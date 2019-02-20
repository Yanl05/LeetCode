class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # if len(cost) == 2:
        #     return min(cost[0], cost[1])
        # dp = [0 for i in range(len(cost)+1)]
        # print(dp)
        # for i in range(2, len(cost)+1):
        #     dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        # return dp

        # 小的往前走一步
        f1 = f2 = 0
        # for x in reversed(cost):
        for x in cost:
            # reversed 返回一个反转的迭代器。
            f1, f2 = x + min(f1, f2), f1

        return min(f1, f2)


print(Solution().
      minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
#                      [0, 0, 1, 2, 2,      3,   3, 4, 4, 5, 6]
