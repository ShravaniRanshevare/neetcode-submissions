class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=[False for i in range(len(matrix))]
        cols = [ False for j in range(len(matrix[0]))]
        b = [[False for i in range (len(matrix[0]))]for _ in range (len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]== 0:
                    if rows[i] != True or cols[j] != True:
                        rows[i] = True
                        cols[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i]==True or cols[j] == True:
                    matrix[i][j]= 0
        
        

        



            
        
        

        
        
        