class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dist = [[-1 for j in range(n)] for j in range(m)]

        Q = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    Q.append([i, j, 0])
            
        nbrs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while Q:
            i, j, currdist = Q.popleft()
            for dx, dy in nbrs:
                if 0 <= i + dx < m and 0 <= j + dy < n and dist[i+dx][j+dy] == -1:
                    dist[i+dx][j+dy] = currdist + 1
                    Q.append([i+dx, j+dy, dist[i+dx][j+dy]])
                    
        return dist
