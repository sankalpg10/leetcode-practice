class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        dist = [[float('inf') for _ in range(n)] for j in range(m)]
        
        dist[start[0]][start[1]] = 0
        Q = collections.deque([start])
        
        nbrs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while Q:
            i, j = Q.popleft()
            for dx, dy in nbrs:
                nx, ny = [i + dx, j + dy]
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0 :
                    nx, ny, rolldist = self.rollball(nx, ny, dx, dy, maze)
                    if dist[i][j] + rolldist < dist[nx][ny]:
                        dist[nx][ny] = dist[i][j] + rolldist
                        Q.append([nx, ny])
                        
        if dist[destination[0]][destination[1]] == float("inf"): return -1
        return dist[destination[0]][destination[1]] 
    
    def rollball(self, x, y, dx, dy, maze):
        m = len(maze)
        n = len(maze[0])
        d = 0505. The Maze II
        while 0 <= y < n and 0 <= x < m and maze[x][y] != 1:
            y += dy
            x += dx
            d += 1

        return x - dx, y - dy, d
