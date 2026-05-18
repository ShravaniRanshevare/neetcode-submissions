# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        length=0
        leftDepth=0
        rightDepth=0
        node = root
        if node.left or node.right:
            
            if node.left:
                leftDepth = self.maxDepth(node.left) 
            else:
                leftDepth=0  
                    
            if node.right:
                rightDepth= self.maxDepth(node.right) 
            else:
                rightDepth=0
        length += 1 + max(leftDepth,rightDepth)
            
        
        return length