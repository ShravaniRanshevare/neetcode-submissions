class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n] +=1
        sorted_list = dict(sorted(d.items(), key= lambda x : x[1],reverse=True)[:k])
        return list(sorted_list.keys())
        
