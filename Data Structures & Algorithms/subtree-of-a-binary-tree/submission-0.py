# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        i,j=p,q
        flag=True
        if (i is None) and (j is None):
            return True
        if (i is None and j is not None) or (j is None and i is not None):
            return False
        
        if i.val != j.val:
            flag=False
        else:
            flag1 = isSameTree(i.left,j.left) 
            flag2 = isSameTree(i.right,j.right)
            if flag1 is False or flag2 is False:
                flag = False
            
        return flag


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        p,q=root,subRoot
        queue= [p]
        visited = []
        while queue:
            node = queue.pop(0)
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        flag=False
        for n in visited:
            flag = isSameTree(n,q)
            if flag == True:
                return flag

        return flag
