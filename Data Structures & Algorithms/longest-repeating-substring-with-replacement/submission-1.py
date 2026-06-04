from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            # add current char
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            # if window is invalid (too many replacements needed)
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # update result
            res = max(res, r - l + 1)

        return res


            

