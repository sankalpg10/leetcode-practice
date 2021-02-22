class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints): return sum(cardPoints)
        
        currSum = sum(cardPoints[-k:])
        maxSum = currSum
        i = 0
        while k > 0:
            currSum = currSum - cardPoints[-k] + cardPoints[i]
            maxSum = max(maxSum, currSum)
            i += 1
            k -= 1
            
        return maxSum
        
        
