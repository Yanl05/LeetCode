class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        retstr = ''
        ret = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j])
                if not ret[i + j]:
                    ret[i + j] = tmp
                else:
                    ret[i + j] += tmp
        for i in range(len(ret)):
            # print(ret[i])
            if ret[i] >= 10:
                ret[i], ret[i + 1] = ret[i] % 10, ret[i + 1] + ret[i] // 10
            retstr += str(ret[i])
        retstr = retstr[::-1]
        if retstr[0] == '0':
            retstr = retstr[1::]
        # print(type(retstr[0]))
           
        
        return retstr
