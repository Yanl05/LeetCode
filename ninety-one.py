class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s == '' or s[0] == '0':
        #     return 0
        # dp = [1, 1]
        # for i in range(2, len(s)+1):
        #     if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0':
        #         dp.append(dp[i-1]+dp[i-2])
        #     elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
        #         dp.append(dp[i-2])
        #     elif s[i-1] != '0':
        #         dp.append(dp[i-1])
        #     else:
        #         return 0
        # return dp[len(s)]



        if s[0] == '0':
            return 0
        l = len(s)
        dp = [0] * l
        dp[0] = 1
        for i in range(1, l):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if '09' < s[i-1:i+1] < '27':
                dp[i] += (dp[i-2] if i > 1 else 1)
        return dp[l-1]


print(Solution().numDecodings("1000"))