class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def dfs(grid, row, col):
            nr = len(grid)
            nc = len(grid[0])
            
            if row < 0 or row >= nr or col < 0 or col >= nc or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dfs(grid, row - 1, col)
            dfs(grid, row + 1, col)
            dfs(grid, row, col - 1)
            dfs(grid, row, col + 1)
        
        if not grid or len(grid) == 0:
            return  0
        
        numislands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numislands += 1
                    dfs(grid, i, j)
                    
        return numislands
    
