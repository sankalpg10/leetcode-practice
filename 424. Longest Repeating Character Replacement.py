class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = collections.defaultdict(int)
        maxFrequency = 0 # maximum frequency among frequency of all characters at current moment
        for i in range(len(s)):
            counts[s[i]] += 1 # increment frequence of current char
            if counts[s[i]] > maxFrequency: # if currenct chars freq > maxFreq then maxFreq = currChar freq
                maxFrequency = counts[s[i]]
            else:
                if i >= maxFrequency + k: # maxFrequency + k = max possible Length at the moment if i (the end point) is at the edge of this window then decrement frequency of starting char as it just got removed due to length constraints
                    counts[s[i-maxFrequency-k]] -= 1 # we have to decrement the frequency because if we do not decrement the frequency and the same char appears in future then it would altercate maxFreq. if there are more than k numbers between the start char and that later appearing char then it is not possible to have that long string
                    
        return min(len(s), maxFrequency + k)

# better variable names
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = collections.defaultdict(int)
        maxFrequency = 0
        for i, char in enumerate(s):
            counts[char] += 1
            if counts[char] > maxFrequency:
                maxFrequency = counts[char]
            else:
                start = s[i - maxFrequency - k]
                currLen = maxFrequency + k
                if i >= currLen:
                    counts[start] -= 1
                    
        return min(len(s), maxFrequency+k)
