class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_dict = len(wordDict)
        len_s = len(s)
        dp = [0] * len_s
        for i in range(len_s):
            for j in range(len_dict):
                len_j = len(wordDict[j])
                if i+1 >= len_j and wordDict[j] == s[i+1-len_j:i+1] \
                        and (i+1-len_j == 0 or dp[i-len_j] == 1):
                    dp[i] = 1
                    break
        return dp[len_s-1] == 1




print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))