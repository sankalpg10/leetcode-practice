class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindromeLen(s, l, r):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                
            return r - l - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = palindromeLen(s, i, i)
            len2 = palindromeLen(s, i, i+1)
            currLen = max(len1, len2)
            if currLen > end - start:
                start, end = i - (currLen - 1)//2, i + currLen//2
        
        return s[start:end+1]
