class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lens = len(strs)
        if lens == 0:
            return ""
        maxprelen = len(strs[0])
        maxpre = strs[0]
        if maxpre.strip()=="":
                return ""
        for i in range(1, lens):
            temp = strs[i]
            if temp.strip()=="":
                return ""

            j = 0
            while maxpre[j] == temp[j]:
                j += 1
                if j >= min(len(maxpre), len(temp)):
                    break
            if j == 0:
                return ""
            if j < maxprelen:
                maxpre = maxpre[0:j]
                maxprelen = j
        return maxpre
