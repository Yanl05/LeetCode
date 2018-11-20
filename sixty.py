class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """
        最高位可以取{1, 2, 3, 4}，而每个数重复3! = 6次。所以第k=9个permutation的s[0]为{1, 2, 3, 4}中的第9/6+1 = 2个数字s[0] = 2。

        而对于以2开头的6个数字而言，k = 9是其中的第k’ = 9%(3!) = 3个。而剩下的数字{1, 3, 4}的重复周期为2! = 2次。所以s1为{1, 3, 4}中的第k’/(2!)+1 = 2个，即s1 = 3。

        对于以23开头的2个数字而言，k = 9是其中的第k” = k’%(2!) = 1个。剩下的数字{1, 4}的重复周期为1! = 1次。所以s[2] = 1.

        对于以231开头的一个数字而言，k = 9是其中的第k”’ = k”/(1!)+1 = 1个。s[3] = 4

        """
        # ans = ''
        # fact = [1]*n
        # num = [str(i) for i in range(1, 10)]
        # for i in range(1, n):
        #     fact[i] = fact[i-1] * i
        # k -= 1
        # for i in range(n, 0, -1):
        #     first = k // fact[i-1]
        #     k %= fact[i-1]
        #     ans += num[first]
        #     num.pop(first)
        # return ans

        FAC = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        res = 0
        k -= 1
        nums = list(range(1, n+1))
        for i in range(n):
            # divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
            # cs 商 k 余数
            cs, k = divmod(k, FAC[n-i-1])
            res = 10*res + nums[cs]
            del nums[cs]
        return res
    # 超时。先全排列再取出第k个转化为str
    #     self.nums = [i for i in range(1, n+1)]
    #     self.res = []
    #     subList = []
    #     self.dfs(self.nums, subList)
    #     ans = self.res[k-1]
    #     strans = ''
    #     for i in ans:
    #         strans += str(i)
    #     return strans
    # def dfs(self, nums, subList):
    #     if len(nums) == len(subList):
    #         self.res.append(subList[:])
    #     for i in nums:
    #         if i in subList:
    #             continue
    #         subList.append(i)
    #         self.dfs(nums, subList)
    #         subList.remove(i)






print(Solution().getPermutation(9, 1))
