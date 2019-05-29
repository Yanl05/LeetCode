# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-05-26 12:30
# @Author  : yanlei
# @FileName: one-hundred-thirty-six.py
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = nums[0]
        for i in range(1, len(nums)):
            tmp = tmp ^ nums[i]
            print(tmp)

        return tmp



print(Solution().singleNumber([2,2,1]))