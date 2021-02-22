class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1  2  3  4
        
        """
        n = len(nums)
        ans = [0]*n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = nums[i-1]*ans[i-1]
        
        R = 1
        for i in range(n-1, -1, -1):
            
            ans[i] *= R
            R *= nums[i]
        
        return ans
