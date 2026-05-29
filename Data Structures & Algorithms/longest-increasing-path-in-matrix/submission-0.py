class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxi=[]
        memo={}
        def backtrack(i,j,prev):
            if i>=len(matrix) or i<0 or j>=len(matrix[0]) or j<0:
                return 0
            if matrix[i][j] <= prev:
                return 0 
            if (i,j) in memo:
                return memo[(i,j)]
         
            res = 1
            d =[(0,1),(-1,0),(1,0),(0,-1)]
            for di,dj in d:
                res = max(res,1 + backtrack(i+di,j+dj,matrix[i][j]))
            memo[(i,j)]=res
            return res
            
        return max(backtrack(i,j,float("-inf")) for i in range(len(matrix)) for j in range(len(matrix[i])))

        

