class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        b = '1'
        for i in range(n - 1):
            a = b[0]
            c = ''
            count = 0
            for j in b:
                if a == j:
                    count += 1
                else:
                    count = str(count) + a
                    c = c + count
                    a = j
                    count = 1
            count = str(count) + a
            c = c + count
            b = c
        return b
