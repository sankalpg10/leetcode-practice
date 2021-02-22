class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        perim = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    perim += 4
                
                    if row > 0 and grid[row-1][col] == 1:
                        perim -= 2

                    if col > 0 and grid[row][col-1] == 1:
                        perim -= 2
                    
        
        return perim
        """
        # dfs solution but unecessary for this problem
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            if grid[row][col] == 0:
                return 1
            if grid[row][col] == -1: return 0
            
            grid[row][col] = -1
            tperim = dfs(row-1, col)
            bperim = dfs(row+1, col)
            lperim = dfs(row, col-1)
            rperim = dfs(row, col+1)
            
            return tperim + bperim + lperim + rperim
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return dfs(row, col)
        """
