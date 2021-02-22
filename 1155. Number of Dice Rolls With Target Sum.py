# O(d*target) | O(d*target)
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
            0 1 2 3 4 5 6 7 -> t
        0   1 0 0 0 0 0 0 0
        1   0 1 0 0 0 0 0 0
        2   0 1 1 0 0 0 0 0
        |
        d
        
        recurrence:
        base case:
        DP[0][0] = 1 if 0 dice left AND target is 0 then 1 way to do it
        DP[0][t] = 0 if 0 dice left and target > 0 then 0 ways to do it
        DP[d][t] = 0 if remaining target is less than 0
        
        General case:
        DP[d][t] = DP[d-1][t-1] + DP[d-1][t-2] + ... + DP[d-1][t-f]
        i.e. number of ways to reach target t with d dice is equal to total number of ways to reach to t-1 with d-1 roles + total ways to reach t-2 with d-1 roles and so on for all face values.        
        """
        
        DP = [[0]*(target+1) for _ in range(d+1)]
        DP[0][0] = 1
        
        for dices in range(1, d+1):
            for t in range(0, target+1):
                DP[dices][t] = 0
                
                for face in range(1, f+1):
                    if t - face < 0: break
                    DP[dices][t] += DP[dices-1][t-face]
                    
        return DP[d][target] % (10**9 + 7)


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = dict()
        def backtrack(d, target):
            
            if target == 0 and d == 0:
                return 1
            if target > 0 and d == 0:
                return 0
            if target < 0: return 0
            
            if (d, target) in memo: return memo[(d, target)]
            memo[(d, target)] = 0
            for i in range(1, f+1):
                memo[(d, target)] += backtrack(d-1, target-i)
        
            return memo[(d, target)]
        
        count = backtrack(d, target)
        return count % (10**9 + 7)
