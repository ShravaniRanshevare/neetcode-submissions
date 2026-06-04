class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(low,high,target,n):
            if low>high:
                return -1
            mid = (low+high)//2
            if n[mid] == target:
                return mid
            elif n[mid] < target:
                return binary(mid+1,high,target,n)
            else:
                return binary(low,mid-1,target,n)
            return -1
        
        for n in matrix:
            low,high=0,len(n)-1
            res = binary(low,high,target,n)
            if res != -1:
                return True
        return False
