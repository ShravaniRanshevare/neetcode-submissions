class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for n in digits:
            num = num*10+n
        num += 1
        output=[]
        for n in str(num):
            output.append(int(n))
        return output
        