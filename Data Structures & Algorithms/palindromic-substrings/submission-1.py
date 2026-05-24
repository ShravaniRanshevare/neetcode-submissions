class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        if not s:
            return 0
        def expandAroundCenter(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res.append(s[left:right+1])
                left -= 1
                right += 1
            

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            expandAroundCenter(i, i)
            # Even length palindrome
            expandAroundCenter(i, i+1)
        return len(res)
 