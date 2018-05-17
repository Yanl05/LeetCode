class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        lend = len(digits)
        res = []
        if lend==0:
            return res
        elif lend==1:
            return list(dic[digits[0]])
        else:
            result = self.letterCombinations(digits[0:lend-1])
            for i in result:
                for j in dic[digits[-1]]:
                    res.append(i+j)
        return res
