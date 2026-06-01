class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        main=[]
        i = 0
        if len(intervals)<1:
            main.append(newInterval)
            return main

        while i< len(intervals) and intervals[i][1]< newInterval[0]:
            main.append(intervals[i])
            i += 1
        main.append(newInterval)
        for j in intervals[i:]:
            a = main[-1]
            if a[1] < j[0]:
                main.append(j)
            else:
                main.pop()
                start = min(a[0],j[0])
                maxend= max(a[1],j[1])
                main.append([start,maxend])

        return main