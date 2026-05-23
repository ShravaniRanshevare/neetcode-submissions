class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges==[]:
            return True
        flag=True
        graph = {i:[] for i in range(n)}
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        #number of edges so that edges=nodes-1
        #cycle ie if u revisit a node while being on its path
        # not connected node counts at the end of traversal dont match
      #add double way edges undirected !!1
        if len(edges) != n-1:
            return False
        node_count = 0
        visited=set()
        
        def dfs(node,prev,visited):
            if node in visited and node != prev:
                return False
            visited.add(node)
            if graph[node]:
                for n in graph[node]:
                    dfs(n,node,visited)

            return True


        flag = dfs(edges[0][0],-1,visited)
        
        if flag and (len(visited) == n):
            return True
        else:
            return False
        
