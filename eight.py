class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #  isdigit() 判断是否为数字，   str[0].isalpha() 判断是否为字母
        str = str.strip()
        lens = len(str)
        s = ''
        count = 0
        if str=="":
            return 0
        if not str[0].isdigit() and str[0] != '-' and str[0] != '+':
            return 0
        if str[0] == '-' or str[0] == '+':
            for i in range(1, lens):
                if str[i].isdigit():
                    s = s + str[i]
                    if i == lens - 1:
                        if str[0] == '-':
                            count = (-1)*int(s)
                            break
                        else:
                            count = int(s)
                            break

                else:
                    if i == 1:
                        return 0
                    else:
                        if str[0] == '-':
                            count = (-1)*int(s)
                            break
                        else:
                            count = int(s)
                            break
            if count < (-1)*(2**31):
                return -2147483648
            elif count > (2 ** 31)-1:
                return 2147483647
            else:
                return count
        else:
            for i in range(0, lens):
                if str[i].isdigit():
                    s = s + str[i]
                    if i == lens - 1:
                        count = int(s)
                        break
                else:
                    count = int(s)
                    break
            if count > (2 ** 31)-1:
                return 2147483647
            else:
                return count
