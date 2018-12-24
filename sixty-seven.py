class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # # 击败60%
        # # 将小的数赋值给a
        # if int(a) > int(b):
        #     a, b = b, a
        # stra = str(a)[::-1]
        # strb = str(b)[::-1]
        # if len(strb) > len(stra):
        #     stra += '0'*(len(strb)-len(stra))
        # # print(int(stra[0])+int(strb[0]))
        # plus = 0
        # res = ''
        # for i in range(len(stra)):
        #     if int(stra[i])+int(strb[i])+plus == 3:
        #         plus = 1
        #         res += '1'
        #     elif int(stra[i])+int(strb[i])+plus == 2:
        #         plus = 1
        #         res += '0'
        #     elif int(stra[i])+int(strb[i])+plus == 1:
        #         plus = 0
        #         res += '1'
        #     elif int(stra[i])+int(strb[i])+plus == 0:
        #         plus = 0
        #         res += '0'
        # # print(res)
        # if plus == 1:
        #     res += '1'
        # return res[::-1]



        # 二进制转十进制 int(a, 2)
        # 击败100%
        num = int(a, 2) + int(b, 2)
        ans = bin(num)
        return ans[2:]

print(Solution().addBinary('111', '1010'))