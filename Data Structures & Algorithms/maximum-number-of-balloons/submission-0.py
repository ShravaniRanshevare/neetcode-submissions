class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        s = "balloon"
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        res = len(text)
        for c in s:
            res = min(res,count[c]//freq[c])
        return res

