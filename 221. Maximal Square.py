class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0
        
         1  1  1  1  0  0
         1  1  2  1  0  0
         1  1  3  2  1  0
         1  1  2  2  1  0
         0  0  1  1  1  0
         0  0  0  0  0  0 
        """
        
        m, n = len(matrix), len(matrix[0])
        DP = [[int(matrix[i][j]) if (i < m and j < n) else 0 for j in range(n+1)] for i in range(m+1)]
        
        maxLen = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if DP[i][j] == 0: continue
                DP[i][j] += min(DP[i][j+1], DP[i+1][j+1], DP[i+1][j])
                maxLen = max(DP[i][j], maxLen)
        
        return maxLen * maxLen
