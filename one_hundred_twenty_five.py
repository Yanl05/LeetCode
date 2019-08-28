# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-28 16:41
# @Author  : yanlei
# @FileName: one_hundred_twenty_five.py

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        newStr = ''
        for item in s:
            if item.isdigit() or item.isalpha():
                # print(item)
                if item.isalpha():
                    item = item.lower()
                newStr += item
        lennewstr = len(newStr)
        if lennewstr % 2 == 0:
            return newStr[:(lennewstr/2)] == newStr[(lennewstr/2):][::-1]
        else:
            # print(newStr[:(lennewstr//2)],newStr[(lennewstr//2)+1:][::-1])
            return newStr[:(lennewstr//2)] == newStr[(lennewstr//2)+1:][::-1]



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))