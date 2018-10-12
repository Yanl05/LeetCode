class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            n = abs(n)
            x = 1 / x
        x0 = x * x
        if n % 2 == 0:
            self.res = self.myPow(x0, n//2)
        else:
            self.res = self.myPow(x0, n//2) * x
        return self.res
