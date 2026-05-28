class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        for src in adj:
            adj[src].sort(reverse=True)  # reverse for efficient pop()

        route = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            route.append(airport)

        dfs("JFK")
        return route[::-1]