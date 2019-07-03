# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-03 09:14
# @Author  : yanlei
# @FileName: four_hundred_thirteen.py

如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数


"""


class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        """

        :param A:
        :return:
        """
        # 暴力解法      -------->   超时
        # # 求子数组的个数
        # N = len(A)
        # all_sum = 0
        # dp = [[0 for _ in range(N)] for _ in range(N)]
        # # 给P Q设定范围
        # for p in range(N-2):
        #     for q in range(p+2, N):
        #         i, j = p, q
        #         # 判断p -> q 是否为等差数列
        #         while q - p >=2:
        #             if A[q]-A[q-1]!=A[q-1]-A[q-2]:
        #                 break
        #             else:
        #                 q=q-2
        #
        #         if q - p <2 and A[p]-A[p+1] == A[p+1]-A[p+2]:
        #             dp[i][j] = 1
        # for item in dp:
        #     all_sum += sum(item)
        # # print(dp)
        # return all_sum

        # 暴力解法 ------> 超时
        # N = len(A)
        # count = 0
        # for p in range(N-2):
        #     # 获得等差的数值
        #     d = A[p+1] - A[p]
        #     for q in range(p+2, N):
        #         tag = True
        #         for i in range(p+1, q+1):
        #             if A[i]-A[i-1]!=d:
        #                 tag = False
        #                 break
        #         if tag:
        #             count+=1
        # return count

    # pass
    #     # 先统计子集个数
    #     if len(A)<3:
    #         return 0
    #
    #     expected = A[1]-A[0]  # 等差的值
    #     count = 0   # 结果数
    #     number = 2  # 子集的大小
    #     for i in range(1, len(A)-1):
    #         # 从第二个元素便利，计算差值
    #         diff = A[i+1]-A[i]
    #         if diff == expected:
    #             number+=1
    #         else:
    #             expected = diff
    #             if number>2:
    #                 count+=self.calculate(number)
    #                 number = 2
    #     if number>2:
    #         count += self.calculate(number)
    #     return count
    # def calculate(self, number):
    #     return sum(range(1,number-1))

        # dp  考虑A[i]为最后元素的等差数组，累加求和
        # dp, sum, d1 = 0, 0, A[1]-A[0]
        # N = len(A)
        # for i in range(2, N):
        #     d2 = A[i]-A[i-1]
        #     if d2 == d1:
        #         dp += 1
        #         sum += dp
        #     else:
        #         dp = 0
        #     d1 = d2
        # return sum

        # dp
        N =len(A)
        dp = [0]*N
        for i in range(2, N):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        print(dp)
        return sum(dp)



print(Solution().numberOfArithmeticSlices([1,2,3,4,5]))