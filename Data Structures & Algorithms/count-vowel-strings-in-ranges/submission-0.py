class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a","e","i","o","u"}
        prefix = [0]*(len(words)+1)
        prev = 0
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefix[i+1] = prev
        
        res = [0] * len(queries)
        for i,q in enumerate(queries):
            l,r = q
            res[i] = prefix[r+1]-prefix[l]
        return res 