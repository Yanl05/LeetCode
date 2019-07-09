# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-09 10:29
# @Author  : yanlei
# @FileName: four_hundred_ninety_one.py

给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
"""

import copy
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #     # dfs
    #     res = set()
    #     self.dfs(nums, 0, res, [])
    #     print(res)
    #     return map(list, res)
    #
    # def dfs(self, nums, index, res, path):
    #     if len(path) >=2:
    #         res.add(tuple(path))
    #     for i in range(index, len(nums)):
    #         if not path or nums[i] >= path[-1]:
    #             self.dfs(nums, i+1, res, path+[nums[i]])

        # dp
        # 初始化字典
        d = {i:[[nums[i]]] for i in range(len(nums))}
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>=nums[j]:
                    for l in d[j]:
                        d[i].append(l+[nums[i]])
        print(d)

        # 处理字典
        res = set()
        for i in range(len(nums)):
            tmp_list = d[i]
            for item in tmp_list:
                if len(item) > 1:
                    res.add(tuple(item))
        return map(list, res)





print(Solution().findSubsequences([4, 6, 7, 7]))