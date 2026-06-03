class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pretty sure per cell call some function if it returns True add it to result
        #dfs 
        #if one cell leads to more cell eventually leads to ocean that ones a winner and how to choose ? only traverse these cell to a neighboring cell with height equal or lower. 
         
        def dfs(i:int ,j:int,visit,prevHeight):
            if i<0 or i>=len(heights) or j<0 or j>=len(heights[0]) or (i,j) in visit or heights[i][j] <prevHeight:
                return 
            hes = heights[i][j]
            visit.add((i,j))
            d = [ (1,0),(-1,0),(0,1),(0,-1)]
            for di,dj in d:
                ni,nj = i+di,j+dj
                dfs(ni,nj,visit,hes)
            
        pac = set()
        atl = set()
        m=len(heights)-1
        n = len(heights[0])-1
        for s in range(len(heights[0])):
            dfs(0,s,pac,heights[0][s])
            dfs(m,s,atl,heights[m][s])

        for v in range(len(heights)):
            dfs(v,0,pac,heights[v][0])
            dfs(v,n,atl,heights[v][n])

        res=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j ) in atl:
                    res.append((i,j))
        
        return res
        

        




            

        
            
            
