class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #so last is -1
        #and for the others at each step u get the max from that num onward and change that
        ans = [0]*len(arr)
        rightMax = -1
        for i in range(len(arr)-1,-1,-1):
            ans[i] = rightMax
            rightMax = max(arr[i],rightMax)
        
        return ans 