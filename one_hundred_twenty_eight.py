# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-11 09:13
# @Author  : yanlei
# @FileName: one_hundred_twenty_eight.py
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 排序   垃圾代码
        # if len(nums) == 0 or len(nums) == 1:
        #     return len(nums)
        # nums.sort()
        # max_value = 0
        # max_sequence = 0
        # for index, item in enumerate(nums):
        #     if index == 0:
        #         max_sequence = 1
        #         if max_value < max_sequence:
        #             max_value = max_sequence
        #         continue
        #     if item - nums[index - 1] == 0:
        #         continue
        #     if item - nums[index - 1] == 1:
        #         max_sequence += 1
        #
        #     else:
        #         if max_value < max_sequence:
        #             max_value = max_sequence
        #         max_sequence = 1
        #     if max_value < max_sequence:
        #         max_value = max_sequence
        # return max_value

        # 排序
        # if not nums:
        #     return 0
        # nums.sort()
        #
        # longest_streak = 1
        # current_streak = 1
        #
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:  # 如果遇到nums[i] nums[i+1] 相等，则直接跳过
        #         if nums[i] == nums[i - 1] + 1:
        #             current_streak += 1
        #         else:
        #             longest_streak = max(longest_streak, current_streak)
        #             current_streak = 1
        # return max(longest_streak, current_streak)

        # 哈希表和线性空间的构造
        longest_streak = 1
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak


print(Solution().longestConsecutive([1, 2, 0, 1]))
print(Solution().longestConsecutive([0, 0]))
