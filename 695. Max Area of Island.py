class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxArea = max(maxArea, self.dfs(grid, [i, j], visited, 1))
                    
        return maxArea
    
    def dfs(self, grid, pos, visited, area):
        nr = len(grid)
        nc = len(grid[0])
        visited[pos[0]][pos[1]] = True
        
        for nbr in self.neighbors(pos, nr, nc):
            if grid[nbr[0]][nbr[1]] == 1 and not visited[nbr[0]][nbr[1]]:
                area = self.dfs(grid, nbr, visited, area+1)
        
        return area
    
    def neighbors(self, pos, nr, nc):
        dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for dx, dy in dxdy:
            nx, ny = [pos[0]+dx, pos[1]+dy]
            if nx >= 0 and nx < nr and ny >= 0 and ny < nc:
                yield nx, ny
                
        
