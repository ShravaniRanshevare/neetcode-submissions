class Node:
    def __init__(self,n):
        self.val=n
        self.distance=0
        self.adj=dict()
    def addEdge(self,node,weight):
        self.adj[node]=weight

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap=[]
        nodes=[]
        for i in range(1,n+1):
            i = Node(i)
            i.distance=float("inf")
            nodes.append(i)
        for t in times:
            start = nodes[t[0]-1]
            target = nodes[t[1]-1]
            start.addEdge(target,t[2])
        
        nodes[k-1].distance=0
        start=nodes[k-1]
        heapq.heappush(heap,(start.distance,k-1))
        #shortest dist = best first, djikstra this one
        visited=[]
        while heap:
            dist,index = heapq.heappop(heap)
            if index in visited:
                continue
            visited.append(index)
            d = nodes[index].adj
            for nei in d:
                new_distance = nodes[index].distance + d[nei]
                if new_distance<nei.distance:
                    nei.distance=new_distance
                    heapq.heappush(heap,(nei.distance,nei.val-1))
        
        if len(visited) < n :
            return -1
        return max(node.distance for node in nodes)
        

