class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        heap=[]
        for h,p in zip(heights,names):
            heapq.heappush(heap,(-h,p))
        
        for _ in range(len(heights)):
            res.append((heapq.heappop(heap)[1]))
        
        return res 
        