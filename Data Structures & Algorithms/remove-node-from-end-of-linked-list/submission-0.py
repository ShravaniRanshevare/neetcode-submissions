# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            head=None
            return head
        length=0
        p=head
        while p:
            p=p.next
            length +=1
        index = length-n
        prev=None
        if index == 0:
            return head.next
        p=head
        for i in range(0,index):
            prev=p
            p=p.next
        next_node=p.next
        prev.next=next_node
        return head
        
