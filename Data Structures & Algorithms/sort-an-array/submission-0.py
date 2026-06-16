class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums)//2
            pivot = nums[mid]
            list1,med,list2=[],[],[]
            for n in nums:
                if n < pivot:
                    list1.append(n)
                elif n == pivot:
                    med.append(n)
                else:
                    list2.append(n)
            return quicksort(list1) + med + quicksort(list2)
        
        res = quicksort(nums)
        return res 