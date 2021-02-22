class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        cost = lambda a, b: abs(ord(b) - ord(a))
        budget = maxCost
        maxLen = 0
        n = len(s)
        l, r = 0, 0
        while r < n:
            currCost = cost(s[r], t[r])
            if s[r] == t[r] or currCost <= budget:
                if s[r] != t[r]: budget -= currCost
                maxLen = max(maxLen, r - l + 1)
                r += 1
            elif l == r:
                l += 1
                r += 1
            else:
                if s[l] != t[l]: budget += cost(s[l], t[l])
                l += 1
                
        return maxLen
