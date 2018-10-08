class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.diag = len(matrix[0])
        # step 1:
        for i in range(self.diag):
            for j in range(i, self.diag):
                self.swap_mat1(i, j, matrix)
        # print(matrix)
        # step 2
        sym = self.diag // 2
        i = 0
        # # 对称轴不动
        # if self.diag % 2 != 0:
        #     while i < sym:
        #         for j in range(self.diag):
        #             self.swap_mat2(i, j, i, matrix)
        #         i += 1
        # # 对称轴也要交换的情况
        # else:
        #     while i < sym:
        #         for j in range(self.diag):
        #             self.swap_mat2(i, j, i, matrix)
        #         i += 1
        while i < sym:
            for j in range(self.diag):
                self.swap_mat2(j, i, i, matrix)
            i += 1


        # print(matrix)
        
    def swap_mat1(self, n1, n2, matrix):
        matrix[n1][n2], matrix[n2][n1] = matrix[n2][n1], matrix[n1][n2]
        # return
    def swap_mat2(self, n1, n2, i, matrix):
        matrix[n1][n2], matrix[n1][self.diag - i - 1] = matrix[n1][self.diag - i - 1], matrix[n1][n2]

