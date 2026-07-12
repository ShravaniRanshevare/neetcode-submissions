class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #so per elem in nums1 u find vohi index pe elem in nums2 then find voh ka num ka immediate greater if no then -1
        def immediate(numindex):
            num = nums2[numindex]
            for i in range(numindex+1,len(nums2)):
                if num<nums2[i]:
                    return nums2[i]
            return -1
        
        map = {}
        for n in range(len(nums2)):
            map[nums2[n]] = immediate(n)
        res = []
        for i in nums1:
            res.append(map[i]) #know they exist cz subset
        
        return res 

            
