import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        heap = []
        for n in range(len(nums)):
            heapq.heappush(heap,(-nums[n],n))
            if n >= k-1 : #k-1 basically the last index of first window so essentially once first window passed
                while heap[0][1] <= n - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res