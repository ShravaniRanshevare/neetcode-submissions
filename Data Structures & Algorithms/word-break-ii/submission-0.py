class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #go thru work break 1 first
        #maybe u start iterating where dp[i] is true ie a word from dic
        #add a space there continue and remove space 
        wordSet = set(wordDict)

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordSet:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        cur = []
        res = []
        backtrack(0)
        return res 