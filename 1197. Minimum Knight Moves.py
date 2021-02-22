class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        q = collections.deque([[0, 0, 0]])
        nbrs = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        visited = {(0, 0)}
        while q:
            cx, cy, steps = q.popleft()
            if cx == x and cy == y: return steps
            
            for dx, dy in nbrs:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) in visited: continue
                visited.add((nx, ny))
                q.append([nx, ny, steps+1])
