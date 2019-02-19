class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        def fibo(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                result = cache[n]
            else:
                result = fibo(n-1) + fibo(n-2)
                cache[n] = result
            return result
        return fibo(N)

print(Solution().fib(5))