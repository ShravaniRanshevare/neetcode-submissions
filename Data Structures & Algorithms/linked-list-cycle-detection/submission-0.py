#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        p = head
        while p:
            if p not in visited:
                visited.add(p)
                p = p.next
            else:
                return True
        return False
            

        
