"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
        
        exhausted=dict()
        def dfs(node,exhausted):
            copy = Node(node.val)
            exhausted[node]=copy
            if node.neighbors:
                for n in node.neighbors:
                    if n not in exhausted:
                        dfs(n,exhausted)
                    copy.neighbors.append(exhausted[n])
        dfs(node,exhausted)
        return exhausted[node]