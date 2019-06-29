# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-29 11:12
# @Author  : yanlei
# @FileName: five_hundred_sixty.py

给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。

"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s:
        :rtype: int
        """
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]

        for lensub in range(1, size+1):  # substring 的长度 1-size
            for i in range(size - lensub+1):  # substring 的起始位置
                j = i + lensub - 1
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        print(dp)
        return dp[0][size-1]





print(Solution().longestPalindromeSubseq('bbbab'))