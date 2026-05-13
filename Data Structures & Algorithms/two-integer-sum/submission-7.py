class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       index={}
       for j in range(len(nums)):
        if nums[j] not in index:
            index[nums[j]]= [j]
        else:
            index[nums[j]] += [j]

       for i in range(len(nums)) :
        c = target - nums[i]
        if c in index:
            if i == index[c][0] and len(index[c]) == 1:
                continue
            if len(index[c])>1:
                if i == index[c][0]:
                    main = index[c][1]
                else:
                    main = index[c][0]
            else:
                main = index[c][0]
            return sorted([i,main])
        else:
            pass
       return []