class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #i left pointer 
        #r right pointer 
        good = set()
        flag = False
        res = []
        for t in triplets:
                two = t
                if two[0]>target[0] or two[1]>target[1] or two[2]>target[2]:
                    continue
                for i,v in enumerate(t):
                    if v == target[i]:
                        good.add(i)

        return len(good) == 3


            
