# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self,curr,k):
        while curr and  k > 0:
            curr = curr.next
            k-=1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev=dummy
        curr = head
        length = 0
        while True:
            n = k
            kth = self.getKth(groupPrev,n)
            if not kth:
                break
            groupNext = kth.next
            prev,curr = kth.next,groupPrev.next
            while curr != groupNext:
                next_node = curr.next
                curr.next=prev
                prev = curr
                curr = next_node
            next_node = groupPrev.next
            groupPrev.next = kth
            groupPrev= next_node
        return dummy.next

            
