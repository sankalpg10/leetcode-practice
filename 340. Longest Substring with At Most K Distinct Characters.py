class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        n = len(s)
        charCounts = collections.defaultdict(int)
        numDistinctChars = 0
        longestLen = 0
        l, r = 0, 0
        while r < n:
            if charCounts[s[r]] > 0 or numDistinctChars < k:
                charCounts[s[r]] += 1
                numDistinctChars += charCounts[s[r]] == 1
                r += 1
                longestLen = max(longestLen, r - l)
            else:
                charCounts[s[l]] -= 1
                numDistinctChars -= charCounts[s[l]] == 0
                l += 1
                
        return longestLen
