class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        allCosts = [0] * n
        allCosts[n-1] = cost[n-1]
        allCosts[n-2] = cost[n-2]
        # tabulation
        for i in range(n-3, -1, -1):
            allCosts[i] = cost[i] + min(allCosts[i + 1], allCosts[i + 2])
        
        return min(allCosts[0], allCosts[1])
    
"""
# memoization
def climb(step):
    if step == n-1 or step == n-2: return cost[step]
    if allCosts[step] != -1: return allCosts[step]

    allCosts[step] = cost[step] + min(climb(step+1), climb(step+2))

    return allCosts[step]
"""
