class Solution:
    def jump(self, nums: List[int]) -> int:
        
        currCov = 0
        lastJumpPos = 0
        numJumps = 0
        n = len(nums)
        if n == 1: return 0
        
        for i in range(n):
            currCov = max(currCov, i + nums[i])
            
            if i == lastJumpPos:
                lastJumpPos = currCov
                numJumps += 1
                if lastJumpPos >= n-1:
                    return numJumps
                
        return numJumps
