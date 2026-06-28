class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #create a hashmap of people and whom they trust
        #whoeevres is empty and whosin everyones is the judge 
        def trusted(d,elem):
            for k in d:
                if elem not in d[k]:
                    return False
            return True
        
        hashed = {}
        for t in trust:
            if t[0] not in hashed:
                hashed[t[0]] = [t[1]]
            else:
                hashed[t[0]].append(t[1])
        
        for i in range(1,n+1):
            if i not in hashed:
                if trusted(hashed,i):
                    return i
        return -1 