class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda word:word[0])
        prevEnd=intervals[0][1]
        count = 0
        for i in intervals[1:]:
            if prevEnd>i[0]:
                prevEnd= min(prevEnd,i[1])
                count += 1
            else:
                prevEnd = i[1]
            
        return count