class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        values = []
        for c in s:
            values.append(ord(c))
        for i in range(len(values)-1):
            res += abs(values[i+1]-values[i])
        
        return res 