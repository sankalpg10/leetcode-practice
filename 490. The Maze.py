from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:                    
        
        def dfs(maze, currpos, destination, visited):
            
            if visited[currpos[0]][currpos[1]]: return False
            if currpos == destination: return True
            
            visited[currpos[0]][currpos[1]] = True
            u, d, l, r = (currpos[0]-1, currpos[0]+1, currpos[1]-1, currpos[1]+1)
            
            while r < len(maze[0]) and maze[currpos[0]][r] == 0:
                r += 1
            if dfs(maze, [currpos[0], r-1], destination, visited):
                return True
            
            while l >= 0 and maze[currpos[0]][l] == 0:
                l -= 1
            if dfs(maze, [currpos[0], l+1], destination, visited):
                return True
            
            while u >= 0 and maze[u][currpos[1]] == 0:
                u -= 1
            if dfs(maze, [u+1, currpos[1]], destination, visited):
                return True
            
            while d < len(maze) and maze[d][currpos[1]] == 0:
                d += 1
            if dfs(maze, [d-1, currpos[1]], destination, visited):
                return True
            
            return False
        
        def bfs(maze, start, destination):
            
            q = deque([start])
            visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
            
            while q:
                currpos = q.popleft()
                if visited[currpos[0]][currpos[1]]: continue
                if currpos == destination: return True
                
                visited[currpos[0]][currpos[1]] = True
                u, d, l, r = [currpos[0]-1, currpos[0]+1, currpos[1]-1, currpos[1]+1]
                
                while l >= 0 and maze[currpos[0]][l] == 0:
                    l -= 1
                q.append([currpos[0], l+1])
                
                while r < len(maze[0]) and maze[currpos[0]][r] == 0:
                    r += 1
                q.append([currpos[0], r-1])
                
                while u >= 0 and maze[u][currpos[1]] == 0:
                    u -= 1
                q.append([u+1, currpos[1]])
                
                while d < len(maze) and maze[d][currpos[1]] == 0:
                    d += 1
                q.append([d-1, currpos[1]])
                
        
        #visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        return bfs(maze, start, destination)
