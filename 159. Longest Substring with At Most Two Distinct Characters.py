class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        charCounts = collections.defaultdict(int)
        numDistinctChars = 0
        longestLen = 0
        l, r = 0, 0
        while r < n:
            if charCounts[s[r]] > 0 or numDistinctChars < 2:
                charCounts[s[r]] += 1
                numDistinctChars += charCounts[s[r]] == 1
                r += 1
                longestLen = max(longestLen, r - l)
            else:
                charCounts[s[l]] -= 1
                numDistinctChars -= charCounts[s[l]] == 0
                l += 1
                
        return longestLen
