class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #so based on query[j] we find if an smallest interval exists which has this num
        #and add that length to output
        intervals.sort(key = lambda i : i[0])
        heap = []
        res = dict()
        i = 0
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0] <= q:
                leng = intervals[i][1]-intervals[i][0]+1
                heapq.heappush(heap,(leng,intervals[i][1]))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        return [res[q] for q in queries]
            
            