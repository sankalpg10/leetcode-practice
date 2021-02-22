class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        nums.sort()
        
        lessThanTargetSums = 0
        
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s >= target:
                    k -= 1
                else:
                    lessThanTargetSums += k - j # if we find three such numbers whose sum is less than target then all the numbers before kth number together with jth number and ith number would sum less than target which would be total of k - j numbers. Therefore we can just add that numebr and move on by incrementing j
                    j += 1
            
        return lessThanTargetSums
    
