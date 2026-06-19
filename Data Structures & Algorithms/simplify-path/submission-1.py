class Solution:
    def simplifyPath(self, path: str) -> str:
        #basically .. means remove last directory
        #one dot ignore same dir 
        res = ""
        stack = []
        sample = [item for item in path.split("/") if item]
        for n in sample:
            if n == "..":
                if stack:
                    stack.pop()
            elif n == ".":
                pass
            else:
                stack.append(n)
        if stack:
            for word in stack:
                res+= "/" + word 
        else:
            res += "/"
        
        return res
            