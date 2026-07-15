class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0 #extra parthenses (
        stack = []
        for i in s:
            if i == "(":
                res.append(i)
                count += 1
            elif i == ")" and count>0:
                res.append(i)
                count -= 1
            elif i != ")":
                res.append(i)
        
        filtered = []
        for c in reversed(res):
            if c == "(" and count>0:
                count -= 1
            else:
                filtered.append(c)
        
        return "".join(reversed(filtered))