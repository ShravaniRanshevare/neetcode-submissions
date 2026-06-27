class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            #here ofc its a 1 cant be 0 prev check
            if grid[i][j] == "#": #visited
                return 0
            f = [(0,1),(0,-1),(1,0),(-1,0)]
            perim = 0
            grid[i][j] = "#" #mark as visited
            for di,dj in f:
                perim += dfs(i+di,j+dj)
            return perim
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]: #not 0 
                    return dfs(i, j)
        return 0