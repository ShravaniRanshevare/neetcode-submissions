class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        l1=0
        l2=0
        idx = 0
        while idx < m + n :#basiaclly len(nums1)
            if l2 >= n or (l1 < m and temp[l1] <= nums2[l2]):
                nums1[idx] = temp[l1]
                l1 += 1
                
            else:
                nums1[idx] = nums2[l2]
                l2 += 1
            idx += 1

