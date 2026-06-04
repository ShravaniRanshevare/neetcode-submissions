class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #this and the previous u start from boundary cells 
        run = set()
        m = len(board)-1
        n = len(board[0])-1
        for i in range(len(board[0])):
            if board[0][i] == "O":
                if (0,i) not in run:
                    run.add((0,i))
            if board[m][i] == "O":
                if (m,i) not in run:
                    run.add((m,i))
        for j in range(1,len(board)-1):
            if board[j][0] == "O":
                if (j,0) not in run:
                    run.add((j,0))
            if board[j][n] == "O":
                if (j,n) not in run:
                    run.add((j,n))
        
        def dfs (i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != "O":
                return
            board[i][j] = "#"
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for di,dj in directions:
                ni,nj=i+di,j+dj
                dfs(ni,nj)
            
        for i,j in run:
            
            dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        

        

        