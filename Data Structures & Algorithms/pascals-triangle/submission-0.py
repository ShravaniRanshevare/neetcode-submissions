class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #it always starts with 1 and ends with 1 
        res = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows): #cz 1,(1,1),then we start 
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


