"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==1:
            return 1
        min_so=0
        start=[]
        end=[]
        res=0
        
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s=0
        e=0
        while s<len(start):
            if start[s]<end[e]:
                s += 1
                min_so += 1
                res=max(res,min_so)
            else:
                min_so -=1
                e += 1
            
        return res
        