class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        n, l, r = len(nums), 0, 0
        maxErasure = 0
        currErasure = 0
        uniqueSet = set()
        
        while r < n:
            if nums[r] not in uniqueSet:
                currErasure += nums[r]
                uniqueSet.add(nums[r])
                r += 1
                maxErasure = max(maxErasure, currErasure)
            else:
                uniqueSet.remove(nums[l])
                currErasure -= nums[l]
                l += 1
                
        return maxErasure
