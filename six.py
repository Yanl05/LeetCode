class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "":
            return ""
        if numRows == 1:  #  由于numRows下面有减2的操作 所以要先判断numRows=1的情况
            return s
        t = []
        for i in range(numRows):
            t.append('')
        lists = list(s)
        while lists:
            for i in range(numRows):
                if lists:
                    t[i] = t[i] + lists[0]
                    del lists[0]
                else:
                    return ''.join(t)
            for j in range(numRows - 2):
                if lists:
                    t[numRows - 2 - j] = t[numRows - 2 - j] + lists[0]
                    del lists[0]
                else:
                    return ''.join(t)
        return ''.join(t)
