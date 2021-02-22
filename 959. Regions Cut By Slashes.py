class Solution:
    
    def regionsBySlashes(self, grid: List[str]) -> int:
        height = len(grid)
        width = len(grid[0])
        self.visited = [[[False for _ in range(4)] for _ in range(width)] for _ in range(height)] # making a boolean grid that keeps track of each visited cell type within a cell
        numRegions = 0
        for i in range(height):
            for j in range(width):
                for t in range(4):
                    if not self.visited[i][j][t]:
                        self.dfs(i, j, t, grid)
                        numRegions += 1
        return numRegions
                        
    def dfs(self, x, y, t, grid):
        
        if not self.inside(x, y, grid) or self.visited[x][y][t]: return
        
        self.visited[x][y][t] = True
        
        if t == 0:
            self.dfs(x-1, y, 2, grid) # topside
        elif t == 1:
            self.dfs(x, y+1, 3, grid) # rightside
        elif t == 2:
            self.dfs(x+1, y, 0, grid) # bottomside
        elif t == 3:
            self.dfs(x, y-1, 1, grid) # leftside
        else:
            raise ValueError
        
        if grid[x][y] != "/":
            self.dfs(x, y, t ^ 1, grid)
        if grid[x][y] != "\\":
            self.dfs(x, y, t ^ 3, grid)
    
    def inside(self, x, y, grid):
        height = len(grid)
        width = len(grid[0])
        return 0 <= x < height and 0 <= y < width
    """
    \.
    .\
    """
          
