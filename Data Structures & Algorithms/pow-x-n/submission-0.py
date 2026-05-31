class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            half = recurse(x,n//2)
            if n%2 == 0:
                return half * half
            else:
                return half * half * x
            
        if n <0:
            return 1/recurse(x,-n)
        else:
            return recurse(x,n)
        

        
