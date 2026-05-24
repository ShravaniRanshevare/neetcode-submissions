class Solution:
    def longestPalindrome(self,s: str) -> str:
        if not s:
            return ""
        
        def expandAroundCenter(left,right):
            while left >= 0 and right < len(s) and s[left]== s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        longest = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i,i)
            even = expandAroundCenter(i,i+1)

            candidate = odd if len(odd)>len(even) else even
            if len(candidate)> len(longest):
                longest = candidate
        return longest

        