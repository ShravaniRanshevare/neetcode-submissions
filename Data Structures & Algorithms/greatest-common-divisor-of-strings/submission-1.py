class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if str1+str2 != str2+str1:
            return res
        g = math.gcd(len(str1), len(str2))
        return str1[:g]
