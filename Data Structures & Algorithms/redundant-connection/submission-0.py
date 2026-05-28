class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # each node is its own parent
        self.rank = [0] * n                  # rank/size for balancing

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False  # cycle detected
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        main=[]
        n = len(edges)
        
        def hasCycle(n,edges):
            dsu = DSU(n+1)
            for u,v in edges:
                if not dsu.union(u,v):
                    main.append([u,v])
        
        hasCycle(n,edges)
        
        if len(main)>1:
            ans = [edges[-1][0],edges[-1][1]]
            return ans
        else:
            return main[0]

