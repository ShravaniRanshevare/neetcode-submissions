class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #isnt it just binary search ?
        hashm= {}
        def get(i):
            if i not in hashm:
                hashm[i] = mountainArr.get(i)
            return hashm[i]
        l = mountainArr.length()
        def binaryAsc(low,high):
            while low <= high:
                mid = low + (high-low)//2
                elem = get(mid)
                if elem == target:
                    return mid
                elif elem>target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1 

        def binaryDsc(low,high):
            while low <= high:
                mid = low + (high-low)//2
                elem = get(mid)
                if elem == target:
                    return mid
                elif elem>target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1 
        
        low = 0
        high = l-1
        while low < high:
            mid = low + (high-low)//2
            elem = get(mid)
            nxt = get(mid+1)
            if elem<nxt:
                low = mid + 1
            else:
                high = mid
           
        pivot = low
        
        res = binaryAsc(0,pivot)
        if res != -1:
            return res
        #right side not sorted its descending when searching in desc do ulta 
        return binaryDsc(pivot+1,l-1)
        #now just binary search from 0 to pivot and pivot +1 to l 