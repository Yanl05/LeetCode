class Solution:
    def solveSudoku(self, board):
        # self.board = board
        self.dfs(board)
    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.check(row, col, board) and self.dfs(board):
                            # print(board)
                            return True
                        board[row][col] = '.'
                    return False
        return True
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
    def check(self, x, y, board):
        tmp = board[x][y]
        board[x][y] = '.'
        for row in range(9):
            if board[row][y] == tmp:
                return False
        for col in range(9):
            if board[x][col] == tmp:
                return False
        for row in range(3):
            for col in range(3):
                if board[3*(x // 3) + row][3*(y // 3) + col] == tmp:
                    return False
        board[x][y] = tmp
        return True

    
