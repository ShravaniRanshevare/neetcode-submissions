class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        if prerequisites == []:
            return True
        for i in prerequisites:
            graph[i[1]].append(i[0])
        visited=set()
        visiting=set()
        unvisited= set(graph.keys())
        def dfs (node,visited,visiting,unvisited):
            if node in visited:
                return True
            elif node in visiting:
                return False
            else:
                unvisited.remove(node)
                visiting.add(node)
                if graph[node] != []:
                    for n in graph[node]:
                        if not dfs(n,visited,visiting,unvisited):
                            return False
                visiting.remove(node)
                visited.add(node)
                return True
        for i in prerequisites:
            if i[0] not in visited:
                if not dfs(i[0],visited,visiting,unvisited):
                    return False
        return True
            
           
            

