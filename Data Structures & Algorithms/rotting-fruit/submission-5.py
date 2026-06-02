from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #minute basically num of rounds of iterations
        #maybe same concept of bfs as traversal from rotten fruit
        count = 0
        queue= []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            sample = queue
            queue = []
            for sam in sample:
                i,j = sam
                for di,dj in directions:
                    ni,nj= i+di,j+dj
                    if 0 <= ni < len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]==1:
                        grid[ni][nj] = 2
                        queue.append((ni,nj))
            if queue:
                count += 1
        for row in grid:
            if 1 in row:
                return -1
        return count
        

        
