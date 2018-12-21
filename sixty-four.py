# 动态规划
class Solution:

    # # 击败97%
    # def minPathSum(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     if not grid or len(grid[0]) == 0:
    #         return 0
    #     m = len(grid)
    #     n = len(grid[0])
    #     return self.minWay(grid, m, n)
    # def minWay(self, grid, m, n):
    #     memo = [[0] * n for _ in range(m)]
    #     memo[0][0] = grid[0][0]
    #     # 从两边开始
    #     for i in range(1, m):
    #         memo[i][0] = memo[i-1][0] + grid[i][0]
    #     for j in range(1, n):
    #         memo[0][j] = memo[0][j-1] + grid[0][j]
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             memo[i][j] = min(memo[i][j-1] + grid[i][j],
    #                              memo[i-1][j]+grid[j][j])
    #     return memo[-1][-1]


    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))