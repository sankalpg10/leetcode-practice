class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        
        closestSum = float("inf")
        for i in range(len(nums)):
            j, k = i + 1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                
                
                closestSum = s if abs(s - target) < abs(closestSum - target) else closestSum
                if closestSum == target: return closestSum

        return closestSum
