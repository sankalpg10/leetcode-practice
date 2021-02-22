class Solution:
    #dfs
    def countServers(self, grid: List[List[int]]) -> int:
        
        def dfs(cell):
            grid[cell[0]][cell[1]] = 0
            numCCs = 1
            for x in range(len(grid)):
                if grid[x][cell[1]] == 1:
                    numCCs += dfs((x, cell[1]))
            
            for y in range(len(grid[0])):
                if grid[cell[0]][y] == 1:
                    numCCs += dfs((cell[0], y))
            
            return numCCs
        
        totalConnectedComputers = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numCCs = dfs((i,j))
                    totalConnectedComputers += 0 if numCCs == 1 else numCCs
                    
        return totalConnectedComputers
 
# non dfs
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        def isConnected(cell):
            x, y = cell
            right = y + 1
            left = y - 1
            up = x - 1
            down = x + 1
            while right < len(grid[0]):
                if grid[x][right] == 1:
                    return True
                right += 1
                                
            while left >= 0:
                if  grid[x][left] == 1:
                    return True
                left -= 1
                
            while down < len(grid):
                if grid[down][y] == 1:
                    return True
                down += 1
                
            while up >= 0:
                if grid[up][y] == 1:
                    return True
                up -= 1
        
            return False
                
            
        totalConnectedComputers = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and isConnected((i, j)):
                    totalConnectedComputers += 1    
                    
        return totalConnectedComputers
