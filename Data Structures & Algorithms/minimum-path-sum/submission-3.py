class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        memo = dict()
        def dfs(i,j):
            if i>=m or i<0 or j>=n or j<0:
                return float("inf")
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m-1 and j == n-1:
                return grid[i][j]
            res = grid[i][j]+ min(dfs(i+1,j),dfs(i,j+1))
            memo[(i,j)] = res
            return res
            
        
        return dfs(0,0)
        
