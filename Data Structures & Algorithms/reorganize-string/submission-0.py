
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s :
            return ""
        #if one word has 2 duplicates and if theres not other two duplicates then there can be made no arrangement
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        maxi = max(freq)

        if maxi > (len(s)+1)//2:
            return ""
        
        res = []
        while len(res)<len(s):
            maxIdx = freq.index(max(freq))
            char = chr(maxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] -= 1
            if freq[maxIdx] == 0:
                continue
            tmp = freq[maxIdx]
            freq[maxIdx]= float("-inf")
            nextMaxIdx = freq.index(max(freq))
            char = chr(nextMaxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] = tmp
            freq[nextMaxIdx] -= 1
        
        return ''.join(res)

        
        
