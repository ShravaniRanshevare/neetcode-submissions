from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #i think if we do same as group anagrams then
        #i create a dict of s1 and then with the length of s1 is my window for ietrating s2

        #suppose l s1 r s2 we iterate thru s2 and
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:n])

        if s1_count == window_count:
            return True

        for i in range(n, m):
            window_count[s2[i]] += 1
            window_count[s2[i-n]] -= 1
            if window_count[s2[i-n]] == 0:
                del window_count[s2[i-n]]

            if window_count == s1_count:
                return True

        return False