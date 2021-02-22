class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l, r, n, k = 0, 0, len(s), len(t)
        if k > n: return ""
        minIndex = -1 # minIndex = -1 if no answer found
        minLen = inf # minLen = inf if no answer found
        surplus = collections.defaultdict(int) # keep tabs of all the chars
        numNegs = 0 # number of missing chars to make window valid
        for char in t: 
            surplus[char] -= 1 # initialize surplus using chars in t
            if surplus[char] == -1: numNegs += 1
        
        while True:
            if numNegs == 0: # if window valid
                if r - l < minLen: minLen, minIndex = r - l, l # if currlen is less than minlen, change minlen and minind
                surplus[s[l]] -= 1 # start minimizing window from left
                if surplus[s[l]] == -1: numNegs += 1 # if deficit then increase num of negatives
                l += 1
            else: # if window is in valid try increasing window size and until window becomes valid or r is out of array
                if r == n: break # if out of array break
                surplus[s[r]] += 1 # increase the surplus[s[right most char]]
                if surplus[s[r]] == 0: numNegs -= 1 # if deficit is filled then decrease num of negatives
                r += 1
        
        return s[minIndex : minIndex + minLen] if minLen != inf else "" # return "" if not found
