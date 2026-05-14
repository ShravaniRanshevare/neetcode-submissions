class Solution:
    def isPalindrome(self,s: str) -> bool:
        s=s.lower()
        empty=""
        for w in s:
            if not w.isalnum():
                pass
            else:
                empty += w
        L=0
        R= len(empty)-1
        while L<=R:
            if empty[L] != empty[R]:
                return False
            else:
                pass
            L +=1
            R -=1
        return True