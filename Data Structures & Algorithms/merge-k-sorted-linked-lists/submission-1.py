import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        elif lists == [[]]:
            return None
        heap = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        dummy = ListNode(0)
        tail = dummy

        while heap:
            val,i,mini = heapq.heappop(heap)
            tail.next=mini
            tail=tail.next
            if mini.next:
                heapq.heappush(heap,(mini.next.val,i,mini.next))
        return dummy.next


