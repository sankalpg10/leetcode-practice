class Solution:
    def maxPower(self, s: str) -> int:
        
        currChar = s[0]
        maxLen = 1
        currLen = 1
        l, r = 0, 1
        while r < len(s):
            if s[r] != s[l]:
                l = r
            else:
                maxLen = max(maxLen, r - l + 1)
                
            r += 1
        
        return maxLen
