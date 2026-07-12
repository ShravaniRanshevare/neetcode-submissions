class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a,b = None,None
        freq = dict()
        end = n**2
        for i in range(1,end+1):
            freq[i] = 0
        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] += 1
        
        for k in freq:
            if freq[k] == 2:
                a = k
            elif freq[k] == 0:
                b = k
        
        return [a,b]