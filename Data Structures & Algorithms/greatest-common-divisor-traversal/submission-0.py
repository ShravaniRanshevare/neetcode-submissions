class UnionFind:
    def __init__(self,n):
        self.n = n
        self.par = [ i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self,v):
        if v != self.par[v]:
            self.par[v] = self.par[self.par[v]]
            
        return self.par[v]
    
    def union(self,v1,v2):
        p1,p2 = self.find(v1),self.find(v2)
        if p1 == p2:
            return False
        self.n -= 1
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.rank[p1] += self.rank[p2]
        self.par[p2] = p1
        return True

    def isConnected(self):
        return self.n == 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        #my idea i have a feeling tht idk if u do if gcd(i,j)>1 then union inshort dfs cz u just wanna check if u can travserse all nodes but u can only traverse if u gcd 
        #or u just for for every i for every i + 1 if gcd()>1 then return true 
        uf = UnionFind(len(nums))
        factor_index = {} # f -> index of value with factor f
        for i,n in enumerate(nums):
            f = 2
            while f*f <= n:
                if n %f == 0:
                    if f in factor_index:
                        uf.union(i,factor_index[f]) #share the same factor gcd so union connect
                    else:
                        factor_index[f]=i
                    while n %f == 0:
                        n = n//f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i,factor_index[n]) #passing index of prev f value
                else:
                    factor_index[n]=i
        return uf.isConnected() #basically n == 1 if all r unioned if all share a gcd 

            











