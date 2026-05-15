
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        

        l1= list1
        l2= list2
        head=None
        if l1.val <l2.val:
            head = l1
            l2 = l2
            l1=l1.next
        elif l2.val<l1.val:
            head=l2
            l2=l2.next
            l1=l1
        else:
            head=l1
            l2 = l2
            l1=l1.next
        p=head
        while l1 and l2:
            if l1.val <l2.val:
                p.next=l1
                l1=l1.next
                p=p.next
            else:
                p.next=l2
                l2=l2.next
                p=p.next
        if l1 is not None:
            while l1:
                p.next=l1
                l1=l1.next
                p=p.next
        elif l2 is not None:
            while l2:
                p.next=l2
                l2=l2.next
                p=p.next
                
            
        return head

            
                