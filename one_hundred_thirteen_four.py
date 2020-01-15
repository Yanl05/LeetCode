# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-15 10:05
# @Author  : yanlei
# @FileName: one_hundred_thirteen_four.py

在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gas-station
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 千疮百孔的垃圾逻辑代码
        # def helper(index):
        #     residue = gas[index]
        #     current = index
        #     if index == 0:
        #         end = len(gas)-1
        #     else:
        #         end = index - 1
        #     while residue > 0:
        #         residue = residue - cost[current]
        #         if residue < 0:
        #             return False
        #         index += 1
        #         if index >= len(gas):
        #             current = index - len(gas)
        #         else:
        #             current = index
        #         if current == end:
        #             if residue + gas[current] - cost[current] >= 0:
        #                 return True
        #             else:
        #                 return False
        #
        #         residue = residue + gas[current]
        #
        # start = [0] * len(gas)
        #
        # for i in range(len(gas)):
        #     if gas[i] >= cost[i]:
        #         start[i] = 1
        # # print(start)
        # for index, item in enumerate(start):
        #     if item == 1:
        #         if helper(index):
        #             return index
        # return -1

        # 时间复杂度o(N) 空间复杂度O(1)

        """:arg
        
        如果 sum(gas) < sum(cost) ，那么不可能环行一圈，这种情况下答案是 -1
        """

        # 记录当前油箱的剩余总油量
        curr_tank = 0
        # 油箱里剩下的由
        total_tank = 0

        n = len(gas)
        starting_station = 0
        for i in range(n):
            total_tank = total_tank + gas[i] - cost[i]
            curr_tank = curr_tank + gas[i] - cost[i]
            # if one could'n get here
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]))
print(Solution().canCompleteCircuit([2], [2]))
print(Solution().canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
