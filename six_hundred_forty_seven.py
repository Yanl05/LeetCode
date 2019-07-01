# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-06-28 23:10
# @Author  : yanlei
# @FileName: six_hundred_forty_seven.py

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".


题目思路：
 先从当前位开始判断，一直向右移
"""
import math

class Solution(object):
    # #  先从当前位开始判断，一直向右移 分别判断子字符是否为回文子串  but 会超时
    # def countSubstrings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     sum = 0
    #     for i in range(len(s)):
    #         for j in range(i+1,len(s)+1):
    #             tmp = s[i:j]
    #             if self.isPalindromic(tmp):
    #                 print(tmp)
    #                 sum+=1
    #     return sum
    #
    #
    # def isPalindromic(self,s):
    #     size = len(s)
    #     if size == 1:
    #         return True
    #     new_s = self.addDivide(s)
    #     # 判断是否为回文子串
    #     mid = math.ceil(len(new_s)/2) -1
    #     left = len(new_s)-mid -1
    #     for i in range(left):
    #         if new_s[mid-i-1] != new_s[mid+i+1]:
    #             return False
    #     return True
    #
    #
    #
    # def addDivide(self,s):
    #     ret = '#'
    #     for i in range(len(s)):
    #         ret = ret + s[i] + '#'
    #     return ret

    def countSubstrings(self, s: str) -> int:
        # 通过P数组计算
        sum = 0
        size = len(s)
        if size == 1:
            return 1
        new_s = self.addDivide(s)
        # 获得P数组
        p = [1, 2]
        for i in range(2, len(new_s)):
            tag = 0
            while i-tag>=0 and i+tag < len(new_s) and new_s[i-tag] == new_s[i+tag]:
                tag+=1
            p.append(tag)
        print(p)
        for i in range(1,len(p)-1):
            if i%2==0:
                sum += (p[i]-1)/2
            else:
                sum+= p[i]/2
        return int(sum)



    def addDivide(self,s):
        ret = '#'
        for i in range(len(s)):
            ret = ret + s[i] + '#'
        return ret





print(Solution().countSubstrings('aaa'))
print(Solution().countSubstrings('abc'))