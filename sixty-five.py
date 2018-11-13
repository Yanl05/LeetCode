"""
 解题思路：先将两端的空格去掉，判断开始是否数字，如果不是直接返回False，然后判断是否遇到'.'和‘e'，然后判断'e'以后是否有’+‘，’-‘和’.'。
"""
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 去前后空格
        s = s.strip()
        begin, last = 0, len(s)-1
        # 数字前为 + or - ，首位后移
        if begin < last and (s[begin] == '+' or s[begin] == '-'):
            begin += 1
        num, dot, exp = False, False, False

        while begin <= last:
            # 该字符为数字
            if s[begin] >= '0' and s[begin] <= '9':
                num = True
            # 如果首位为‘.’且s[begin]还为点则返回False，否则标记为小数
            elif s[begin] == '.':
                if dot or exp:
                    return False
                dot = True
            # 同理 e
            elif s[begin] == 'e' or s[begin] == 'E':
                if exp or not num:
                    return False
                exp, num = True, True
            # 判断数中间的'+' or '-'
            elif s[begin] == '+' or s[begin] == '-':
                if s[begin-1] != 'e':
                    return False
            else:
                return False
            begin += 1
        return num





print(Solution().isNumber(".1"))
