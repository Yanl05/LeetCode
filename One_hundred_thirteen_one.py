# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-14 08:44
# @Author  : yanlei
# @FileName: One_hundred_thirteen_one.py

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        split_result = []
        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return
            for end in range(start + 1, len(s) + 1):
                split_s = s[start:end]
                # print(split_s)
                # print(split_s[:][::-1])
                if split_s == split_s[:][::-1]:
                    back(end, res + [split_s])

        back()
        return split_result

    # 判断子串是否为回文串
    def isPalindromic(self, subs):
        """

        :param subs:  subs 子串
        :return:
        """
        # # print(subs)
        # lens = len(subs)
        # if lens == 1:
        #     return True
        # halflens = lens // 2
        # # print(halflens)
        # i = 0
        # while i < halflens:
        #     if subs[i] != subs[lens - i - 1]:
        #         return False
        #     i += 1
        # return True

        left = 0
        right = len(subs) - 1

        while left < right:
            if subs[left] != subs[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().partition("aab"))
