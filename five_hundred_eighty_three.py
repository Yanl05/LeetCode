# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-02 10:20
# @Author  : yanlei
# @FileName: five_hundred_eighty_three.py

给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

莱文斯坦距离

解题思路：
 求莱文斯坦距离。题设中没有替换 只能删除，那么替换的公式
 由
 # 替换，插入，删除
 levab[i][j] = min(levab[i - 1][j - 1] + 1, levab[i][j - 1] + 1, levab[i - 1][j] + 1)
 ----->
 levab[i][j] = min(levab[i - 1][j - 1] + 2, levab[i][j - 1] + 1, levab[i - 1][j] + 1)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        levab = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # 1.计算空字符串到各字符的莱文斯坦距离
        for j in range(len(word2) + 1):
            for i in range(len(word1) + 1):
                if min(i, j) == 0:
                    levab[i][j] = max(i, j)
                    # 如果ai = bj 则不做任何操作 ，莱文斯坦距离等于上一个子串的莱文斯坦距离
                elif word2[j-1] == word1[i-1]:
                    levab[i][j]=levab[i - 1][j - 1]
                else:
                    # 替换，插入，删除
                    levab[i][j] = min(levab[i - 1][j - 1] + 2, levab[i][j - 1] + 1, levab[i - 1][j] + 1)

        return levab[-1][-1]


print(Solution().minDistance('a', 'b'))
