# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 19:05
# @Author  : yanlei
# @FileName: seventy_eight.py

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# # 1.递归
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         n = len(nums)
#
#         def helper(i, tmp):
#             res.append(tmp)
#             print(tmp)
#             for j in range(i, n):
#                 helper(j+1, tmp+[nums[j]])
#
#         helper(0, [])
#         return res
#
# print(Solution().subsets([1, 2, 3]))

# 2.迭代
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            print(i)
            res = res + [num + [i] for num in res]
            print(res)
        return res

print(Solution().subsets([1, 2, 3]))

# 3.库函数
import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                print(tmp)
                res.append(tmp)
        return res

print(Solution().subsets([1, 2, 3]))