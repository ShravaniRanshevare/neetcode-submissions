import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums=nums
        self.heap= []
        for n in self.nums:
            if len(self.heap)<self.k:
                heapq.heappush(self.heap,n)
            else:
                if n > self.heap[0]:
                    heapq.heapreplace(self.heap,n)
        
            

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        else:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap,val)
        return self.heap[0]



        
