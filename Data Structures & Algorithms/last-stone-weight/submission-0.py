class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
                heapq.heappush(heap,-stone) 
        
        
        while len(heap)>=2:
            m1,m2= heapq.heappop(heap),heapq.heappop(heap)
            if m1 == m2:
                continue
            elif m1>m2 or m2>m1:
                elem = abs(m1-m2)
                heapq.heappush(heap,-elem)
            

        if heap:
            return -heap[0]
        return 0 


            