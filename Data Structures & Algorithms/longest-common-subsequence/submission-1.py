class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l = 0
        r = 0
        memo=dict()
        def recurse(l,r) :
            if (l,r) in memo:
                return memo[(l,r)]
            if l>=len(text1) or r>=len(text2):
                return 0
            if text1[l] == text2[r]:
                res=1+ recurse(l+1,r+1) 
                memo[(l,r)]= res
                return res
            else:
                ves = max(recurse(l+1,r),recurse(l,r+1))
                memo[(l,r)]= ves
                return ves
            
        return recurse(l,r)