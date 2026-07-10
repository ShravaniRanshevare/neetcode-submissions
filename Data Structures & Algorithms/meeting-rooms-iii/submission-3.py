class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]  # Min heap for available rooms
        used = []  # Min heap for used rooms [(end_time, room_number)]
        count = [0] * n  # Count of meetings for each room

        for start, end in meetings:
            while used and used[0][0] <= start: #if done make room avaialbl
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                end_time, room = heapq.heappop(used) #if no room available skip time forward
                end = end_time + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room)) #get avaialble room and assign it 
            count[room] += 1

        return count.index(max(count))

