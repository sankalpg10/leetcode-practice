class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        2 1 3
        6 5 4
        7 8 9
        
        -19 57
        -40 -5
        
        Reccurence:
        Base case: 
        cost = matrix of size m*(n+2) initialized on left and right edges with inf
        for 1x1 matrix: cost[0][0] = matrix[0][0]
        cost of last row = cost at that index
        
        general case: cost[i][j] = matrix[i][j] + min(cost[i+1][j+1], cost[i+1][j], cost[i+1][j-1])
        """
        m, n = len(matrix), len(matrix[0])
        cost = [[inf for _ in range(n+2)] for _ in range(m)]
        for i in range(1, n+1):
            cost[m-1][i] = matrix[m-1][i-1]
            
        
        for i in range(m-2, -1, -1):
            for j in range(n, 0, -1):
                cost[i][j] = matrix[i][j-1] + min(cost[i+1][j-1], cost[i+1][j], cost[i+1][j+1])
                
        return min(cost[0])
