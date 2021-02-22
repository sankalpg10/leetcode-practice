class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        currComb = []
        combinations = []
        
        def backtrack(start):
            if len(currComb) == k:
                combinations.append(currComb[:])
                return
            
            for num in range(start, n+1):
                currComb.append(num)
                backtrack(num+1)
                currComb.pop()
                
        backtrack(1)
        return combinations
