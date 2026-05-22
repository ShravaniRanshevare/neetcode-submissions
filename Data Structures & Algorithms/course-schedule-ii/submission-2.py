class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i : [] for i in range(numCourses)}
        for i in prerequisites:
            graph[i[1]].append(i[0])
        def dfs(node,visited,visiting,unvisited):
            if node in visited:
                return True
            elif node in visiting:
                return False
            unvisited.remove(node)
            visiting.add(node)
            if graph[node]:
                for n in graph[node]:
                    if not dfs(n,visited,visiting,unvisited):
                        return False
            visiting.remove(node)
            visited.append(node)
            return True
        visited=[]
        unvisited=set(graph.keys())
        visiting=set()
        for i in graph:
            if i not in visited:
                if not dfs(i,visited,visiting,unvisited):
                    return [] #if cycle hai toh no order pf courses
        visited = visited[::-1]
        
        return visited #order in which they are visited/added with no cycles
        

