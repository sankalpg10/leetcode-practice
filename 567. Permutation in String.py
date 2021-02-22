class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)
        if k > n: return False
        surplus = collections.defaultdict(int)
        
        for char in s1: surplus[char] -= 1
        for i in range(k): surplus[s2[i]] += 1
        if all(surplus[c] == 0 for c in surplus): return True
                    
        for i in range(k, n):
            surplus[s2[i]] += 1
            surplus[s2[i-k]] -= 1
            if all(surplus[c] == 0 for c in surplus): return True
            
        return False
