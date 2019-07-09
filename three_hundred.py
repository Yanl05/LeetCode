# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-09 09:52
# @Author  : yanlei
# @FileName: three_hundred.py

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 时间复杂度 o(n^2)
        # nums = [float('-inf')] + nums
        # dp = [0 for _ in range(len(nums))]
        # for i in range(1, len(nums)):
        #     for j in range(i-1, -1, -1):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1, dp[i])
        # print(dp)
        # return max(dp)

        # 时间复杂度 o(nlogn)
        if not nums:
            return 0
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                j = 0
                while nums[i]>stack[j]:
                    j+=1
                stack[j]=nums[i]

        return len(stack)






print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))