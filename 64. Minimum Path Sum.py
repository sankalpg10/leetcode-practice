class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DP = [[0 for _ in range(n)] for _ in range(m)]
        
        DP[m-1][n-1] = grid[m-1][n-1]
        for col in range(n-2, -1, -1): DP[m-1][col] = grid[m-1][col] + DP[m-1][col+1]
        for row in range(m-2, -1, -1): DP[row][n-1] = grid[row][n-1] + DP[row+1][n-1]
        print(DP)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                DP[i][j] = grid[i][j] + min(DP[i][j+1], DP[i+1][j])
        print(DP)
        return DP[0][0]
