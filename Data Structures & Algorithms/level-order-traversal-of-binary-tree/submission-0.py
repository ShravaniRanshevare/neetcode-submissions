# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        visited = []
        length = 0
        while queue:
            arr = queue
            queue = []
            newlist=[]
            for node in arr:
                newlist.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            visited.append(newlist)
        return visited
        

            
            