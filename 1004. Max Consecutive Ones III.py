class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        n = len(A)
        l, r = 0, 0
        maxSub = 0
        currZeros = 0
        
        while r < n:
            if A[r] == 1 or currZeros < K:
                if A[r] == 0: currZeros += 1
                r += 1
                maxSub = max(maxSub, r-l)
            elif l == r:
                l += 1
                r += 1
            else:
                if A[l] == 0: currZeros -= 1
                l += 1
                
        return maxSub
