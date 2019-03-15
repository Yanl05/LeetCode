class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        temp = [0] * len(primes)
        ret = [1]
        while len(ret) < n:
            premin = float('inf')
            for i in range(len(primes)):
                premin = min(premin, ret[temp[i]]*primes[i])
            ret.append(premin)
            for i in range(len(primes)):
                if ret[-1] == ret[temp[i]]*primes[i]:
                    temp[i] += 1
        return ret[-1]



print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))