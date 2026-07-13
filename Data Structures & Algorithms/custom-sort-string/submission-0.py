class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map=dict()
        for i in range(len(order)):
            map[order[i]] = i
        
        return ''.join(sorted(s,key=lambda c: map.get(c,26)))