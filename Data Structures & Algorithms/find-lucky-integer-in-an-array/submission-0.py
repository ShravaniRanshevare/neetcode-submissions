class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        maxOne = float("-inf")
        for key in count:
            if count[key] == key:
                maxOne = max(maxOne,key)
        
        return maxOne if maxOne != float("-inf") else -1