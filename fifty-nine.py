class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        # 创建n*n矩阵，全部赋值为0
        res = [[0 for x in range(n)] for x in range(n)]
        cnt, choice = 1, 0
        i, j = 0, 0
        weight = 1
        res[0][0] = 1
        while cnt < n*n:
            if choice == 0:
                j += 1
                res[i][j] = cnt + 1
                if j == n - weight:
                    choice = 1
            elif choice == 1:
                i += 1
                res[i][j] = cnt + 1
                if i == n - weight:
                    choice = 2
            elif choice == 2:
                j -= 1
                res[i][j] = cnt + 1
                if j == weight - 1:
                    choice = 3
                    weight += 1
            elif choice == 3:
                i -= 1
                res[i][j] = cnt + 1
                if i == weight - 1:
                    choice = 0
            cnt += 1
        return res


print(Solution().generateMatrix(5))
