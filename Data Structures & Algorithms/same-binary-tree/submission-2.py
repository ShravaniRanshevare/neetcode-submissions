# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        i,j=p,q
        flag=True
        if (i is None) and (j is None):
            return True
        if (i is None and j is not None) or (j is None and i is not None):
            return False
        
        if i.val != j.val:
            flag=False
        else:
            flag1 = self.isSameTree(i.left,j.left) 
            flag2 = self.isSameTree(i.right,j.right)
            if flag1 is False or flag2 is False:
                flag = False
            
        return flag

