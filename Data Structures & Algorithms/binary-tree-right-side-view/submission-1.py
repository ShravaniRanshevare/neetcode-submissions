# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #u start from root ok if it has a right ofc right visible
        #then work ur way down if right has a right or left then that otherwise move to nodes.left
        #one algorithm that helps u go layer by layer bfs
        if root is None:
            return []
        res = []
        queue=[root]
        
        while queue:
            sam = queue
            res.append(sam[-1].val)
            queue = []
            for node in sam:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
                
        
        return res


            