class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def createAdjList(n, edges):
            G = [[] for _ in range(n)]
            for u, v in edges:
                G[u].append(v)
                G[v].append(u)
                
            return G
        
        
        G = createAdjList(n, edges)
        visited = [False]*n
        def visit(v):
            for nbr in G[v]:
                if not visited[nbr]:
                    visited[nbr]=True
                    visit(nbr)
        
        numCC = 0
        for v in range(n):
            if not visited[v]:
                numCC += 1
                visited[v] = True
                visit(v)
                
        return numCC
