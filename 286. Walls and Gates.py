class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        emptyRoom = 2**31 - 1
        
        Q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    Q.append([i, j, 0])
                    
        nbrs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while Q:
            i, j, currdist = Q.popleft()
            for dx, dy in nbrs:
                
                if 0 <= i + dx < m and 0 <= j + dy < n and rooms[i + dx][j + dy] == emptyRoom:
                    rooms[i+dx][j+dy] = currdist + 1
                    Q.append([i + dx, j + dy, rooms[i+dx][j+dy]])
                    
            
            
        
