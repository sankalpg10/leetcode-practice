from collections import deque
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:            
        
        friendCircles = 0
        visited = [False for _ in range(len(M))]
        for u in range(len(M)):
            if not visited[u]:
                self.dfs(M, u, visited)
                friendCircles += 1
                
        return friendCircles
        
        
       # return self.bfs(M)
    
    def dfs(self, network, u, visited):
        for v in range(len(network)):
            if network[u][v] == 1 and not visited[v]:
                visited[v] = True
                self.dfs(network, v, visited)

    def bfs(self, network):
        visited = [False for _ in range(len(network))]
        friendCircles = 0
        q = deque()
        for u in range(len(network)):
            if not visited[u]:
                q.append(u)
                while q:
                    s = q.popleft()
                    visited[s] = True
                    for v in range(len(network)):
                        if network[s][v] == 1 and not visited[v]:
                            q.append(v)
                friendCircles += 1
                
        return friendCircles
