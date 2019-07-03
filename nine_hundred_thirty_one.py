# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-03 10:47
# @Author  : yanlei
# @FileName: nine_hundred_thirty_one.py

给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

 

示例：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：12
解释：
可能的下降路径有：
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
和最小的下降路径是 [1,4,7]，所以答案是 12。

"""
import copy

class Solution:
    def minFallingPathSum(self, A) -> int:
        dp,dp_1 = len(A[0])*[0],len(A[0])*[0]
        length = len(A)
        wide = len(A[0])
        if wide == 1:
            ant = 0
            for i in range(length):
                # print(A[i])
                ant += A[i][0]
            return ant
        elif wide == 0:
            return 0


        for i in range(length):
            for j in range(wide):
                if j == 0:
                    dp_1[j] = min(A[i][j]+dp[j],A[i][j]+dp[j+1])
                elif j == wide-1:
                    dp_1[j] = min(A[i][j]+dp[j-1],A[i][j]+dp[j])
                else:
                    dp_1[j] = min(A[i][j]+dp[j-1],A[i][j]+dp[j],A[i][j]+dp[j+1])



            # print(dp_1)
            # 此处不能直接赋值 赋值会将两个list指向同一对象
            # dp = dp_1
            # 要深度拷贝，让二者完全独立
            dp = copy.deepcopy(dp_1)
            # print(dp)
        return min(dp)

# print(Solution().minFallingPathSum([[1],[4],[7]]))
# print(Solution().minFallingPathSum([[1]]))
print(Solution().minFallingPathSum([[-80,-13,22],[83,94,-5],[73,-48,61]]))
