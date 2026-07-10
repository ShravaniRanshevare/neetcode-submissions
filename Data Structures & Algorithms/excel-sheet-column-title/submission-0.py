class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet_dict = {i: chr(i + 64) for i in range(1, 27)}
        res = ""
        while columnNumber>0:
            columnNumber -= 1
            offset = columnNumber%26
            res += chr(ord('A')+offset)
            columnNumber //= 26

        return ''.join(reversed(res)) 
