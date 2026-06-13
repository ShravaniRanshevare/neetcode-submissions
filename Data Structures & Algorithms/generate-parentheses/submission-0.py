class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #valid strings r also a part of the problem ie same num of ( and )
        res = []
        stack = []
        openn=0
        close=0
        def dfs(openn,close):
            if openn == close == n:
                res.append("".join(stack))
                return
            if openn<n:
                stack.append("(")
                dfs(openn+1,close)
                stack.pop()
            if close<openn:
                stack.append(")")
                dfs(openn,close+1)
                stack.pop()
            
        dfs(openn,close)
        return res 
