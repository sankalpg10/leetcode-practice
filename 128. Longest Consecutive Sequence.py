class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        
        maxStreak = 0
        for num in hashset:
            if num - 1 not in hashset:
                
                currentnum = num
                currstreak = 1
                while currentnum+1 in hashset:
                    currentnum += 1
                    currstreak += 1
                    
                maxStreak = max(maxStreak, currstreak)
                
        return maxStreak
