class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        x = list(str(x))
        lenx = len(x)
        for i in range(lenx // 2):
            if x[i] != x[lenx - 1 - i]:
                return False
        return True
