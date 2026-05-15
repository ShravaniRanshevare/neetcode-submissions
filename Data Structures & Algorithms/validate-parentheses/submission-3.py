class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}": "{" , ")":"(","]":"["}
        stack = []
        if len(s)<=1:
            return False
        for w in s:
            if w not in valid:
                stack.append(w)
            else:
                if not stack:
                    return False
                if stack.pop() != valid[w]:
                    return False    
        if stack:
            return False
        else: 
            return True