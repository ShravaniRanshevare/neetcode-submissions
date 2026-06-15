class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        def dfs(i,j):
            if i<0  or i>=len(grid) or  j<0 or j>=len(grid[0]):
                return 0

            if grid[i][j]==0:
                return 0
            grid[i][j]=0 #since u dont want traversal again 
            s = 1
            four = [(0,1),(0,-1),(1,0),(-1,0)]
            for di,dj in four:
                s+= dfs(i+di,j+dj)
            return s 

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = max(count,dfs(i,j))
        
        return count 


