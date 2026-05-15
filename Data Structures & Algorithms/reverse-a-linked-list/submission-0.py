# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            prev = None
            p=head
            
            while p:
                next_node = p.next
                p.next=prev
                prev=p
                p=next_node
        return prev
                
        
          