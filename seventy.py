class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2 and n > 0:
            return n
        ways = [0] * (n+1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways [i-1] + ways[i-2]
        return ways[n]
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(5))