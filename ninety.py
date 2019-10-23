# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 19:31
# @Author  : yanlei
# @FileName: ninety.py

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 递归
# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         n = len(nums)
#
#
#         def helper(i, tmp):
#             if tmp not in res:
#                 res.append(tmp)
#                 print(tmp)
#             for j in range(i, n):
#                 helper(j+1, tmp + [nums[j]])
#
#         helper(0, [])
#         return res
#
# print(Solution().subsetsWithDup([1, 2, 2]))

# 迭代
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res if [i] + num not in res]
            # print(tmp)



        return res

print(Solution().subsetsWithDup([1, 2, 2]))