class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num == 1:
        #     return True
        # while num % 2 == 0:
        #     num /= 2
        # while num % 3 == 0:
        #     num /= 3
        # while num % 5 == 0:
        #     num /= 5
        # return num == 1

        if num < 1:
            return False
        while num % 2 == 0:
            return self.isUgly(num//2)
        while num % 3 == 0:
            return self.isUgly(num//3)
        while num % 5 == 0:
            return self.isUgly(num//5)
        return num == 1






print(Solution().isUgly(0))