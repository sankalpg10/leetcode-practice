class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i = j = 0
        maxCount = 0
        currCount = 0
        while j < len(nums):
            if nums[j] == 1:
                currCount += 1
            else:
                currCount = 0
                i = j+1
            maxCount=  max(currCount, maxCount)
            j += 1
            
        return maxCount
