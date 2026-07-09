class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map=dict()
        for i,v in enumerate(s):
            map[v] = i
        res = []
        size = 0
        end = 0
        for i,c in enumerate(s):
            size += 1
            end = max(end,map[c])
            if i == end:
                res.append(size)
                size = 0
        return res 

            
