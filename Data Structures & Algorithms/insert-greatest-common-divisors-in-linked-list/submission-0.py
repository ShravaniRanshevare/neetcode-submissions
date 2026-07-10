# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        p = head
        while p.next:
            curr = p
            n = p.next
            g = gcd(curr.val,n.val)
            curr.next = ListNode(g,n)
            p = curr.next.next
        return head