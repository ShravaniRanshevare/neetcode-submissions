class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def canWe(i,j,board):
            r = i - 1
            while r >=0:
                if board[r][j] == "Q":
                    return False
                r -=1
            r ,c = i-1, j-1
            while r>= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            r,c = i-1,j+1
            while r >=0 and c <len(board[r]):
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            return True


        res = []
        board = [["."] * n for i in range(n)]
        def dfs(row):
            if row == n :
                copy = ["".join(r) for r in board]
                res.append(copy)
                return 
            for j in range(n):
                if canWe(row,j,board):
                    board[row][j] = "Q"
                    dfs(row + 1)
                    board[row][j] = "."
        dfs(0)   
        return len(res)