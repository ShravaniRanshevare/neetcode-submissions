"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        ans = dummy
        nodes = []
        dnodes = dict()
        p = head
        count = 0
        while p:
            val = p.val 
            node=Node(val)
            dnodes[p] = node #stores the og node and its copy
            ans.next = node
            ans = ans.next
            p=p.next
        
        #dummy.next = new
        p=head
        curr=dummy
        while p:
            random = p.random #now i wanna fetch the node from dict
            if random is not None:
                rnode = dnodes[random]
            else:
                rnode= None
            curr.next.random = rnode
            curr = curr.next
            p=p.next
        
        return dummy.next




        