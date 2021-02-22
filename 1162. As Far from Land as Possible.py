class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dist = [[-1 for _ in range(n)] for _ in range(m)]
        
        Q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    Q.append([i, j])
        maxDist = -1  
        nbrs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while Q:
            i, j = Q.popleft()
            for dx, dy in nbrs:
                nx, ny = [i + dx, j + dy]
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[i][j] + 1
                    maxDist=  max(maxDist, dist[nx][ny])
                    Q.append([nx, ny])
                    
        return maxDist
