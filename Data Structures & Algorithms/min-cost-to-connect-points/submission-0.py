class DSU:
    def __init__(self, n:List):
        self.parent = list(range(n))
        self.rank = [0]*n              # rank/size for balancing

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        def manhattan(i,j):
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(i,j)
                edges.append((d,i,j))

        edges.sort()
        dsu = DSU(n)
        cost, used = 0, 0

        for w,u,v in edges:
            if dsu.union(u,v):
                cost += w
                used += 1
                if used == n-1:  # MST complete
                    break
        return cost