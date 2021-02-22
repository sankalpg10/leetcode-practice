class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n-1: return False
        
        G = [[] for _ in range(n)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
            
        vis = [False]*n
        def visit(node):
            for nbr in G[node]:
                if not vis[nbr]:
                    vis[nbr] = True
                    visit(nbr)
        numCC = 0
        for u in range(n):
            if not vis[u]:
                numCC += 1
                vis[u] = True
                visit(u)
        
        return numCC == 1
