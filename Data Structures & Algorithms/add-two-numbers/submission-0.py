# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            p = head
            prev = None
            while p:
                next_node = p.next
                prev = p
                p.next=prev
                p = next_node
            return prev
            
        p,q = l1,l2
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while p or q or carry:
            val1 = p.val if p else 0
            val2 = q.val if q else 0
            total = val1+val2+ carry
            carry = total//10
            digit = total %10
            curr.next = ListNode(digit)
            curr = curr.next
            if p : p=p.next
            if q : q = q.next
        return dummy.next

