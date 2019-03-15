class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t1 = 0
        t2 = 0
        t3 = 0
        # 分别为2，3，5三个因子
        res = [1]
        while len(res) < n:
            res.append(min(res[t1] * 2, res[t2] * 3, res[t3] * 5))
            if res[-1] == res[t1] * 2:
                t1 += 1
            if res[-1] == res[t2] * 3:
                t2 += 1
            if res[-1] == res[t3] * 5:
                t3 += 1
        return res





print(Solution().nthUglyNumber(10))
