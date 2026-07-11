class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #one pointer R at the end if space caharacter then move up -1
        #l starts from the start u move ahead till u find a space caharcter nd then the index + 1 from that
        #if there are any space in that substring move l ahead by that many indices
        r = len(s)-1
        while s[r] == " ":
            r -= 1
        
        l = r
        while l >= 0 and s[l] != " ": #or now uk the end move up till u find space thats ur last word!!!!!
            l -=1
        
        return len(s[l+1:r+1])
        
            
