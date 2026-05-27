class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        res = []
        for i in range(0,n+1):
            res.append(i)
        
        for r in res:
            s= bin(r)[2:]
            count = s.count("1")
            output.append(count)

        return output