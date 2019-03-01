class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1, 1]
        if n <= 1:
            return f[n]
        for i in range(2, n+1):
            tmp = 0
            for j in range(0, i):
                tmp += f[j]*f[i-j-1]
            f.append(tmp)
        return f[n]


print(Solution().numTrees(3))
