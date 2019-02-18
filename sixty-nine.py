class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        其中 x 是非负整数
        :rtype: int
        """
        # 牛顿迭代法
        if x <= 1:
            return x
        r = x
        while r > x/r:
            r = (r + x / r) // 2
        return int(r)
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))