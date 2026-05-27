class Solution:
    def reverseBits(self, n: int) -> int:
        s=0
        for i in range(32):
            bit = n&1
            s = (s << 1)| bit
            n >>=1
        return s
            
        