class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
            
        return lastPos == 0
# the greed here is that we only need to check which is the left most safe index we can reach from last node.
