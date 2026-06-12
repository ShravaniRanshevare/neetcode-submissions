# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        indices = { elem: index for index,elem in enumerate(inorder)}    
        
        #idk while loop
        
        #maybe we check if node has been added or not if not
        #then we create node and from inorder w do node.left node.right i-1 i+1 then move onto next index 
        #check its i-1 i+1 if htreyre alreasyd theyre dont if not connect it 
        self.index = 0
        added = set()
        def dfs(l,r):
            if l>r :
                return None
            val = preorder[self.index]
            node = TreeNode(val)
            self.index += 1
            mid = indices[val]
            node.left = dfs(l,mid-1)
            node.right = dfs(mid+1,r)
            return node
        
        return dfs(0,len(inorder)-1)

        
