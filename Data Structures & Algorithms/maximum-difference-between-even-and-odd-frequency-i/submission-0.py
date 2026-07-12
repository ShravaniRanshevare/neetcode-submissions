class Solution:
    def maxDifference(self, s: str) -> int:
        count = collections.Counter(s)
        #if u pick max odd freq one nd min even freq one 
        #thats max diff
        maxOdd = 0
        minEven = float("inf")
        for k in count:
            if count[k]%2 != 0:
                maxOdd = max(maxOdd,count[k])
            elif  count[k]%2 == 0:
                minEven = min(minEven,count[k])

        return maxOdd - minEven
