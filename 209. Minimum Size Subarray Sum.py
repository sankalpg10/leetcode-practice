class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        n, l, r = len(nums), 0, 0
        minLen = inf
        currSum = 0
        
        while True:
            if currSum >= s:
                minLen = min(minLen, r - l)
                currSum -= nums[l]
                l += 1
            else:
                if r == n: break
                currSum += nums[r]
                r += 1
        
        return minLen if minLen != inf else 0
