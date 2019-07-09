# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-09 09:15
# @Author  : yanlei
# @FileName: six_hundred_forty_six.py

给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

示例 :

输入: [[1,2], [2,3], [3,4]]
输出: 2
解释: 最长的数对链是 [1,2] -> [3,4]
注意：

给出数对的个数在 [1, 1000] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-pair-chain
"""


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = self.list_sort(pairs)
        pairs = [[0,float('-inf')]]+pairs
        # print(pairs)
        dp = [0]*len(pairs)
        for i in range(1,len(pairs)):
            if pairs[i][0] > pairs[i-1][1]:
                dp[i] = dp[i-1]+1
            else:
                for j in range(i-1, -1, -1):
                    if pairs[i][0] > pairs[j][1]:
                        dp[i] = dp[j]+1
                        break
        print(dp)
        return dp[-1]

    def list_sort(self,pairs):
        new_pairs = sorted(pairs, key=lambda x:x[0],reverse=False)
        return new_pairs

print(Solution().findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
))
print(Solution().list_sort([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
))