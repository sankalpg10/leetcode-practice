class Solution:
    def balancedString(self, s: str) -> int:
        
        l, r, n = 0, 0, len(s)
        minChange = inf
        surplus = {'Q': -n//4, 'W': -n//4, 'E': -n//4, 'R': -n//4}
        for c in s: surplus[c] += 1
        if all(surplus[c] == 0 for c in surplus): return 0
        while True:
            if all(surplus[c] <= 0 for c in surplus):
                minChange = min(minChange, r - l)
                surplus[s[l]] += 1
                l += 1
            else:
                if r == n: break
                surplus[s[r]] -= 1
                r += 1
                
        return minChange
