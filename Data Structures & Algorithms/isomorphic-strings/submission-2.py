class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #first both need to have same length
        #two chars cant map to same char for ex a,r = o,o so no
        #dict of each char in s and its counterpart of t
        #if any key has more thna one value false return false when u encounter seocnd one
        #mapping both dir
        if len(s) != len(t):
            return False
        match1 = dict()
        match2 = dict()
        for i in range(len(s)):
           c1, c2 = s[i], t[i]
           if ((c1 in match1 and match1[c1] != c2) or (c2 in match2 and match2[c2] != c1)):
                return False
           match1[c1] = c2
           match2[c2]=c1
        return True


            