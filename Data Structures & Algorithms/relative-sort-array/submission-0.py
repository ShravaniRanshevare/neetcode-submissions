class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_v = max(arr1) #why so that u have all nums slots in arr1 to add the ones not in arr2 later on
        count = [0]*(max_v+1)

        for num in arr1:
            count[num] += 1 #freq of nums
        
        res = []
        for num in arr2:
            res += [num]*count[num]
            count[num] = 0
        
        for num in range(len(count)):
            res += [num] * count[num]
        
        return res 
        
