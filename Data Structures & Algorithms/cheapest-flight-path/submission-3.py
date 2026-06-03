class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #really the only way is prob djikstra but the moment path length > k restart
        #apparently smth bellman ford algo first gotta build the graph
        dist=[float("inf")]*n
        dist[src]=0 #src can be smth else
        graph={i:{} for i in range(n)}
        for i in flights:
            graph[i[0]].update({i[1]:i[2]})
        
        for _ in range (k+1):
            temp=dist[:]
            for u,v,w in flights:
                if dist[u] != float("inf") and temp[v]>dist[u]+w:
                    temp[v]=dist[u]+w
            dist = temp
            
        if dist[dst] == float("inf"):
            return -1
        else:
            return dist[dst]
        

