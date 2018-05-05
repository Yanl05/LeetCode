class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        longestlenth = 1  # 非空子串的长度最小为1
        substr = ''
        for item in s:
            if item not in substr:
                substr += item
            else:
                if len(substr) > longestlenth:
                    longestlenth = len(substr)
                #  把重复的字符添加进去，然后截出出新的substr
                substr += item
                substr = substr[substr.index(item) + 1:]
        if len(substr) > longestlenth:
            longestlenth = len(substr)
        return longestlenth
                
