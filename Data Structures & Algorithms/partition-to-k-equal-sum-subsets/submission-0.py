class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #so num of subarrays u can have is k
        #maybe the sum it shud equal to max elem?
        #same as matchsticks
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)  # optimization
        sides = [0] * k          # k slots (like 4 sides in square)

        def dfs(index):
            if index == len(nums):
                return all(side == target for side in sides)

            for j in range(k):  # try putting nums[index] into any slot
                if sides[j] + nums[index] <= target:
                    sides[j] += nums[index]
                    if dfs(index + 1):
                        return True
                    sides[j] -= nums[index]

                # pruning: if this slot was empty and failed, no point trying others
                if sides[j] == 0:
                    break
            return False

        return dfs(0)