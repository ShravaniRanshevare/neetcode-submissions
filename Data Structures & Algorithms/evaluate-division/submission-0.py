class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        forward = collections.defaultdict(list)
        
        #so for a to c we have a/b and b/c so we do a/b/c/b whose values we do have 
        for i,e in enumerate(equations):
            a,b=e
            forward[a].append((b,values[i]))
            forward[b].append((a,1/values[i]))
            

        def bfs(source,target):
            if source not in forward or target not in forward:
                return -1
            queue,visit = deque([(source,1)]),set()
            visit.add(source)
            while queue:
                node,w = queue.popleft()
                if node == target:
                    return w
                for nei,weight in forward[node]:
                    if nei not in visit:
                        queue.append((nei,w*weight))
                        visit.add(nei)
            return -1

        return [bfs(q[0],q[1]) for q in queries]

            
