class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        allCombSums = []
        currComb = []
        candidates.sort()
        n = len(candidates)
        def backtrack(targetLeft, start):
            if targetLeft == 0:
                allCombSums.append(currComb[:])
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]: continue
                    
                if candidates[i] > targetLeft: break
                currComb.append(candidates[i])
                backtrack(targetLeft - candidates[i], i+1)
                currComb.pop()

        backtrack(target, 0)
        return allCombSums
