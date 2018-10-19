class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [-1 for i in range(n)]
        solution = []
        self.dfs(0, board, [], solution)
        return solution
    def dfs(self, depth, board, valuelist, solution):
        if depth == len(board):
            solution.append(valuelist)
        for row in range(len(board)):
            if self.check(depth, row, board):
                s = '.'*len(board)
                board[depth] = row
                self.dfs(depth+1, board, valuelist+[s[:row]+'Q'+s[row+1:]], solution)

    def check(self, depth, row, board):
        for i in range(depth):
            if board[i] == row or abs(depth-i) == abs(row - board[i]):
                return False
        return True
