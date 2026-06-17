class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag = False
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                sam = s[:i] + s[i+1:]
                if sam == sam[::-1]:
                    flag = True 
        return flag
