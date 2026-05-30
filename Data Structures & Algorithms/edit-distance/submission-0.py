class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i,j=0,0
        copy=word2
        main={}
        def recurse(i,j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if (i,j) in main:
                return main[(i,j)]
            if word1[i] == word2[j]:
                main[(i,j)]= recurse(i+1,j+1)
            else:
                res=float("inf")
                # 3 choices u insert or delete or replace
                ops = [(0,1),(1,0),(1,1)]
                for di,dj in ops:
                    res = min(res, 1 + recurse(i+di,j+dj))
                main[(i,j)] = res
                
            return main[(i,j)]

        return recurse(i,j)