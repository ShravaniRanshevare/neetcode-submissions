

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda word: word[0])
        merged=[intervals[0]]
        for i in intervals[1:]:
            a = merged[-1]
            b = i
            if a[1] < b[0]:
                merged.append(b)
            else:
                merged.pop()
                maxend = max(a[1],b[1])
                merged.append([a[0],maxend])
        return merged
