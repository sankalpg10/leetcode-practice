class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        i, j = 0, 0
        maxVowels = 0
        currVowels = 0
        while j < len(s):
            if j-i == k:
                if s[i] in "aeiou": currVowels -= 1
                i += 1
            currVowels += s[j] in "aeiou"
            maxVowels = max(maxVowels, currVowels)
            j += 1
        
        return maxVowels
