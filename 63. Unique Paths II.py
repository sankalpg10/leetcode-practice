class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0]: return 0
        
        DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
        DP[m-1][n-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1: continue
                if obstacleGrid[i][j] != 1:
                    DP[i][j] = DP[i][j+1] + DP[i+1][j]
                
        return DP[0][0]
