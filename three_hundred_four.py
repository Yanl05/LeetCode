# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-07-13 10:14
# @Author  : yanlei
# @FileName: three_hundred_four.py
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。


上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if len(self.matrix) == 0 or len(self.matrix[0]) == 0:
            return

        dp = [[0 for col in range(len(self.matrix[0])+1)] for row in range(len(self.matrix)+1)]
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                # # 初始化 dp
                # if row == 0 and col == 0:
                #     dp[0][0] = self.matrix[0][0]
                #     continue
                # if row == 0:
                #     dp[0][col] = dp[0][col - 1] + self.matrix[0][col]
                #     continue
                # if col == 0:
                #     dp[row][0] = dp[row - 1][0] + self.matrix[row][0]
                #     continue

                dp[row+1][col+1] = dp[row+1][col] + dp[row][col+1] - dp[row][col] + self.matrix[row][col]
            print(dp)
            self.dp = dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # 超时
        # ret = 0
        # for row in range(row1, row2+1):
        #     ret = ret + sum(self.matrix[row][col1:col2+1])
        # return ret

        # dp缓存行  超时
        # dp = [[0 for _ in range(len(self.matrix[0])+1)] for _ in range(len(self.matrix))]
        # for row in range(len(self.matrix)):
        #     for col in range(len(self.matrix[0])):
        #         dp[row][col+1] = dp[row][col] + self.matrix[row][col]
        #
        # sum = 0
        # for row in range(row1, row2+1):
        #     sum += dp[row][col2+1] - dp[row][col1]
        # # print(sum)
        # return sum

        # dp (row2,col2)-(row2, col1-1)-(row1-1,col2)+(row1-1,col1-1)

        # if row2 == row1 and col1 == col2:
        #     return self.matrix[row1][col1]
        # elif row2 == row1:
        #     return self.dp[row1][col2] - self.dp[row1][col1-1]
        # elif col1 == col2:
        #     return self.dp[row2][col2] - self.dp[row1-1][col2]
        # else:
        #     return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]





# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]


matrix = [
            [-4,-5]
              # [3, 0, 1, 4, 2],
              # [5, 6, 3, 2, 1],
              # [1, 2, 0, 1, 5],
              # [4, 1, 0, 1, 7],
              # [1, 0, 3, 0, 5]
            ]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(0,0,0,1)
print(param_1)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)