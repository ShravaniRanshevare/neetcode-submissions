class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #maybe we have two heaps one main based on enqueue
        #one for processing time
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res, minHeap = [], []
        i, time = 0, tasks[0][0]
        
        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                #so minheap is ur pro time queue 
                #so for all tasks with time reached add them to this so what we did
                i += 1
            if not minHeap:
                #time not reached of first task
                time = tasks[i][0]
            else:
                #minheap has one task whos time and proc time is her
                procTime,index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res 
            






