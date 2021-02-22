class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxGold = 0
        
        def backtrack(x, y, currGold):
            nonlocal maxGold
            maxGold = max(maxGold, currGold)
            
            nbrs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dx, dy in nbrs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:
                    tmp = grid[nx][ny]
                    grid[nx][ny] = 0
                    backtrack(nx, ny, currGold+tmp)
                    grid[nx][ny] = tmp
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                tmp = grid[i][j]
                grid[i][j] = 0
                backtrack(i, j, tmp)
                grid[i][j] = tmp
                
        return maxGold
