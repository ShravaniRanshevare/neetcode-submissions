# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        queue = [root]
        maxso = root.val
        def dfs(node,maxso):
            if not node:
                return 0
            if node.val >= maxso:
                good = 1
            else:
                good = 0
            maxso = max(maxso,node.val)
            return good + dfs(node.left,maxso) + dfs(node.right,maxso)
        return dfs(root,maxso)

        