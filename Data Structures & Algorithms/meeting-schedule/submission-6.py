"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        dp=[False]*(len(intervals)+1)
        dp[0]=True #empty schedule
        def meetings(dp):
            if len(dp)<=1:
                return 
            dp[1]= True #first schedule cannot conflict with prev ones
            for i in range(2,len(intervals)+1):
                a,b= intervals[i-2].start,intervals[i-2].end
                x,y = intervals[i-1].start,intervals[i-1].end
                if b<=x and dp[i-1] == True:
                    dp[i]= True
                else:
                    dp[i]=False
        meetings(dp)        
        return dp[len(intervals)]
            
