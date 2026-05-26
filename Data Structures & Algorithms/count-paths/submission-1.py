class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique=0
        #maybe u do for each grid call dfs which goes thru all neighbours till goal is reached
        #and when each dfs ends count one path?
        memo=dict()
        def dfs(i,j):
            paths=0
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if i ==m-1 and j == n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            paths = dfs(i+1,j) + dfs(i,j+1)
            memo[(i,j)]=paths
            return paths
        

        unique = dfs(0,0)
        return unique