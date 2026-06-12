import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for p in points:
            dist = math.sqrt(((p[0]-0)**2)+((p[1]-0)**2))
            heapq.heappush(heap,(dist,p))
        
        res = []
        for _ in range(k):
            v = heapq.heappop(heap)
            res.append(v[1])
        return res