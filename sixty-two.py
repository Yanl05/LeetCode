class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # # ways[i][j] = ways[i][j-1] + ways[i-1][j]
        # ways = [[1 for i in range(n)] for i in range(m)]
        # print(ways)
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             ways[i][j] = 1
        #         else:
        #             ways[i][j] = ways[i-1][j] + ways[i][j-1]
        # return ways[m-1][n-1]

        # ways[j] = ways[j] + ways[j-1]
        ways = [0]*n
        ways[0] = 1
        for i in range(m):
            for j in range(1, n):
                ways[j] += ways[j-1]
        return ways[n-1]


print(Solution().uniquePaths(7, 3))
