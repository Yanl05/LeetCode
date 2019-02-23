class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1  # 6
        n = len(word2) + 1  # 4
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = i
        for i in range(m):
            dp[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j]+1,
                               dp[i][j-1]+1,
                               dp[i-1][j-1]+(0 if word1[i-1] == word2[j-1] else 1))
        print(dp)
        return dp[m-1][n-1]
print(Solution().minDistance("horse", "ros"))