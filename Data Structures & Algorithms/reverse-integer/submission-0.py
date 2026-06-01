class Solution:
    def reverse(self, x: int) -> int:
        MAX= (2**31) - 1
        MIN = -2**31
        res=0
        num = x
        x = abs(x)
        while x:
            d = x%10
            x /= 10 
            x = int(x)
            
            if res>MAX/10 or res < MIN/10:
                return 0
            if res == MAX/10 and d > MAX%10:
                return 0
            if res == MIN/10 and d<MIN%10:
                return 0
            else:
                res = res*10 + int(d)
        if num <0:
            return -res
        else:
            return res 

