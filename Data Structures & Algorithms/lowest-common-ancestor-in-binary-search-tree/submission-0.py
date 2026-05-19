# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = []
        LCA=None
        i=root
        queue=[i]
        while queue:
            node=queue.pop(0) 
            parents.append(node)
            if node.val:
                if node.val == p.val or node.val == q.val:
                    return node
                if node.val > p.val and node.val>q.val:
                    queue.append(node.left)
                elif node.val<p.val and node.val<q.val:
                    queue.append(node.right)
                elif (node.val>p.val and node.val<q.val) or (node.val<p.val and node.val>q.val):
                    LCA = node
                    return LCA

    