class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        allCombSums = []
        currComb = []
        candidates.sort()
        def backtrack(targetLeft, start):
            if targetLeft == 0:
                allCombSums.append(currComb[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > targetLeft: return
                currComb.append(candidates[i])
                backtrack(targetLeft-candidates[i], i)
                currComb.pop()
            
        backtrack(target, 0)
        return allCombSums
