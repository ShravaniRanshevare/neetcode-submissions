import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #ok curr num == og elevation
        #each iteration or smth represents t
        #swim 4 directions but cant traverse if og elev of both squares is <= t
        #return t ? taken to reach last cell in depth dont have to visit every cell or layer by layer
        #dfs maybe idk what t is 
        #call dfs from 0,0 till u reach ladt somehow
        #u have neighbours pick the one with lowest value thats ur t and from 1 neighbour is 3 which is why t = 3 at the time of termination
        m,n=len(grid),len(grid[0])
        heap=[]
        t=0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        elev = t
        heapq.heappush(heap,(grid[0][0],0,0))
        visited = set()
        while heap:
            cell,i,j = heapq.heappop(heap)
            visited.add((i,j))
            elev = max(elev,cell)
            
            if (i,j) ==  (m-1,n-1):
                return elev
            
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(heap, (grid[ni][nj], ni, nj))
            
        return elev 
            

        

                
            

        



        
                    

            

