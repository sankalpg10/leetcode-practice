class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        10 9 2 5 3 7 101 18
        2  2 4 3 3 2 1   1

        0 1 0 3 2 3
        4 3 3 1 2 1
        
        7 7 7 7 7 7 7
        1 1 1 1 1 1 1
        """
        
        n = len(nums)
        if n==0: return 0
        DP = [0]*n
        DP[-1] = 1
        lastSmallest = nums[-1]
        for i in range(n-2, -1, -1):
            DP[i] = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    DP[i] = max(DP[i], 1 + DP[j])
        
        return max(DP)
