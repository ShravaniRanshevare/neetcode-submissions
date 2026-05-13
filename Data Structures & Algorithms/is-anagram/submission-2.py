class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = []
        set2= []
        if (len(s) != len(t)):
            return False
        for n in range(len(s)):
            set1.append(s[n])
            set2.append(t[n])
        set1.sort()
        set2.sort()
        res = set1==set2
        return res