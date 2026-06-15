class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #we know there r n queens and its nxn board so if n=2
        #ok prob is not attacking each other 
        #2x2 so two rows two columns
        #dir = four usual + daigonal 
        #as i said permuattions 
        board = [["."] * n for i in range(n)]
        res = []

        def canWe(i,j,board):
            row = i-1
            while row >=0:
                if board[row][j] == "Q" :
                    return False
                row -= 1

            #upar ka row -1
            row, col = i - 1, j - 1 #upper left and right diagonal no bottom cz for later on ones added  they will check for themselves upstairs
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = i - 1, j + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True
            
        def dfs(i):
            #just column index 
            if i == n:
                copy = [ "".join(row) for row in board]
                res.append(copy)
                return 
            for j in range(n):
                if canWe(i,j,board):
                    board[i][j]= "Q"
                    dfs(i+1)
                    board[i][j]= "."

        dfs(0)
        return res 


            
    

        
