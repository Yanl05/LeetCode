# -*- coding: UTF-8 -*-

"""
# @Time    : 2020-01-17 09:24
# @Author  : yanlei
# @FileName: one_hundred_forty.py

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # if len(s) == 0 or len(wordDict) == 0:
        #     return []
        # word_set = {word for word in wordDict}
        # dp = [False] * len(s)
        # dp[0] = s[0] in word_set
        #
        # for r in range(1, len(s)):
        #     # 如果整个单词就直接在word_set中，直接返回
        #     # 否则把单词做分割，挨个去判断
        #     if s[:r + 1] in word_set:
        #         dp[r] = True
        #         continue
        #
        #     for l in range(r):
        #         if dp[l] and s[l + 1:r + 1] in word_set:
        #             dp[r] = True
        #             break
        # print(dp)
        #
        # split_s = []
        #
        # # 从尾往首遍历
        # def dfs(end=len(s), sub_str_list=[]):
        #     # 如果最后切分的单词刚好在字典中，那可以直接取出结果
        #     if s[:end] in word_set:
        #         sub_str_list.append(s[:end])
        #         # 因为sub_str_list添加的子串是从s的右边往左边添加的，因为后面有个pop操作，所以这里先复制
        #         sub_str_copy = sub_str_list[:]
        #         sub_str_copy.reverse()
        #         new_str = " ".join(sub_str_copy)
        #         split_s.append(new_str)
        #         sub_str_list.pop()
        #
        #     for start in range(end-1, -1, -1):
        #         # 对应转移方程二
        #         if dp[start] and (s[start+1:end] in word_set):
        #             dfs(start+1, sub_str_list+[s[start+1:end]])
        #
        # dfs()
        # return split_s


print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
