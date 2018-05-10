class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
        """
     
        if x<0:
            num = -1 * int(str(-x)[::-1])
        else:
            num = int(str(x)[::-1])
        if num > 2**31 -1 or num < -(2**31):
            num = 0
        return num
       
