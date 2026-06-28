class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #for each pos suppose u run bfs till u reach the pos target but if u encounter a deadlock at that pos return -1
        #no treat whome string as node
        #neighbours 0000 - 0001,1000,0100,0010 not in deadlock move ahead if u get one go back maybe
        if "0000" in deadends:
            return -1
        queue = [("0000",0)]
        def childrenCombs(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        visited = { dead for dead in deadends} #treat them as visited
        while queue:
            node,turn = queue.pop(0)
            if node == target:
                return turn
            children = childrenCombs(node)
            for c in children:
                if c not in visited:
                    visited.add(c)
                    queue.append((c,turn+1))
        return -1 
            
            

