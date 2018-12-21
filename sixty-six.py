class Solution:
    # # 击败9%
    # def plusOne(self, digits):
    #     """
    #     :type digits: List[int]
    #     :rtype: List[int]
    #     """
    #     lenn = len(digits)
    #     digits = digits[::-1]
    #     ans = 0
    #     for i in range(lenn):
    #         ans = ans + digits[i] * (10**i)
    #     ans += 1
    #     lena = len(str(ans+1))
    #     res = []
    #     for i in range(lena):
    #         res.append(ans//(10**(lena-i-1)))
    #         ans = ans%(10**(lena-i-1))
    #     return res

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 1; ret = []
        for d in digits[::-1]:
            v = d + plus
            if v > 9:
                v = v % 10
                plus = 1
            else:
                plus = 0
            ret.insert(0, v)
        if plus == 1:
            ret.insert(0, plus)
        return ret
print(Solution().plusOne([4,3,2,1]))
