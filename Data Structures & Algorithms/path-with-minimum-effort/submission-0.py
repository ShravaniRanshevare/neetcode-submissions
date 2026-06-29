class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minheap = [(0,0,0)]
        heapq.heapify(minheap)
        
        trow,tcol = len(heights)-1,len(heights[0])-1
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        while minheap:
            effort,row,col = heapq.heappop(minheap)
            if (row,col) in visit:
                continue
            visit.add((row,col))
            if row == trow and col == tcol:
                return effort
            
            for di,dj in neighbours:
                i,j = row+di,col+dj
                if (i<0 or j<0 or i>=len(heights) or j>=len(heights[0]) or (i,j) in visit):
                    continue
                new_ef = max(effort,abs(heights[i][j]-heights[row][col]))
                heapq.heappush(minheap,(new_ef,i,j))
        return 0

