class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #limit of projs = k
        #fund initially w
        #first pick has to be one which has capital <= w infact all of them
        #then based off of this pick max from profit list
        minHeap=[]
        for i,p in enumerate(profits):
            heapq.heappush(minHeap,(capital[i],i,p))
        #now we have a heap ok that will store proj based on how much cap they need
        #I DID ITTTTT
        maxi = 0
        maxHeap=[]
        for _ in range(k):
            while minHeap and minHeap[0][0]<=w:
                cap,idx,prof = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,(-prof,idx))
            if maxHeap:
                prof,idx = heapq.heappop(maxHeap)
                w += - prof 
            else:
                break

        return w 
                
