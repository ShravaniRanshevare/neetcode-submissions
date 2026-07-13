class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time,total=0,0 #current time,total time
        for a,w in customers:
            if time>a:
                total += time-a
            else:
                time = a
            total += w
            time += w
        
        return total/len(customers)


