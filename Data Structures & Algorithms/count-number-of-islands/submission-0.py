class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        groups = 0
        def backtrack(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]):
                return 
            cell = grid[i][j]
            if cell != "1":
                return 
            four = [(-1,0),(0,-1),(0,1),(1,0)]
            grid[i][j]="0"
            for di,dj in four:
                backtrack(i+di,j+dj)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    groups +=1
                    backtrack(i,j)
                    

        return groups