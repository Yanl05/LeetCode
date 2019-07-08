"""
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets
"""
import copy


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        if not len(days):
            return 0
        dp = [0] * (366 + 30)
        dp[days[-1]] = min(costs)

        for j in range(len(days) - 2, -1, -1):
            for i in range(days[j] + 1, days[j + 1]):
                # 8 - 20  i = 9~19的每一天
                # 将没有出行的天数的 costs 赋值为 后一天的 costs
                dp[i] = dp[days[j + 1]]
            # 如果七天的票价 比一天的票价贵
            if costs[0] < costs[1]:
                dp[days[j]] = min(dp[days[j] + 1] + costs[0], dp[days[j] + 7] + costs[1], dp[days[j] + 30] + costs[2])
            else:
                dp[days[j]] = min(dp[days[j] + 7] + costs[1], dp[days[j] + 30] + costs[2])

        print(dp)
        return dp[days[0]]


print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
