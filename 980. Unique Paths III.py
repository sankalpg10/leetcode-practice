class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        def backtrack(row, col, remainingEmpty):
            if grid[row][col] == 2 and remainingEmpty == 1:
                nonlocal count
                count += 1
                return
            temp = grid[row][col]
            grid[row][col] = -2
            remainingEmpty -= 1
            nbrs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for dx, dy in nbrs:
                nrow, ncol = row + dx, col + dy
                if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] >= 0:
                        backtrack(nrow, ncol, remainingEmpty)
                        
            grid[row][col] = temp
        
        emptypath = 0
        srow, scol = 0, 0
        for row in range(m):
            for col in range(n):
                emptypath += grid[row][col] >= 0
                if grid[row][col] == 1:
                    srow, scol = row, col

        backtrack(srow, scol, emptypath)
        return count
                    
