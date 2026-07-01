class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        memo = dict()
        def dfs(i,j):
            if i>=m or i <0 or j>=n or j<0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i== m-1 and j == n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            paths = dfs(i+1,j)+dfs(i,j+1)
            memo[(i,j)] = paths
            return paths

        return dfs(0,0)
            