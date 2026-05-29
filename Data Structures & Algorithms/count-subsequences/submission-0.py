class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def recurse(i,j):
            res,ves,jes=0,0,0
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == t[j]: 
                memo[(i,j)]= recurse(i+1,j+1) + recurse(i+1,j)
            else:
                memo[(i,j)]= recurse(i+1,j)
            return memo[(i,j)]
            
        return recurse(0,0)    