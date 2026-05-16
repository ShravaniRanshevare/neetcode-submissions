# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None :
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev,i=None,slow.next
        slow.next=None
        while i:
            next_node=i.next
            i.next=prev
            prev=i
            i=next_node
        
        p,q=head,prev
        while q:
            next_node=p.next
            l2_next=q.next
            p.next=q
            q.next=next_node
            p=next_node
            q=l2_next
            
            
        