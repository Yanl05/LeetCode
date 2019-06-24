# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-24 14:24
# @Author  : yanlei
# @FileName: three_hundred_and_three.py
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        res_list = []
        tmp = 0
        for index in range(len(self.nums)):
            tmp += self.nums[index]
            res_list.append(tmp)
        self.res_list = res_list


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        # 超时答案
        # res = 0
        # for loc in range(i, j+1):
        #     res += self.nums[loc]
        # return res
        return self.res_list[j] - self.res_list[i] + self.nums[i]





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
print(param_1)

