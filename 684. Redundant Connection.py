class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        G = collections.defaultdict(set)
        
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nbr, target) for nbr in G[source])
            
        for u, v in edges:
            seen = set()
            if u in G and v in G and dfs(u, v):
                return u, v
            G[u].add(v)
            G[v].add(u)
            
"""
u = 1, v = 2
G[1] = {2}
G[2] = {1}
u = 1, v = 3
G[1] = {2, 3}
G[3] = {1}
u = 2, v = 3
dfs(2, 3):
seen = {}
seen = {2}
source != target
dfs(1, 3)
seen = {2}
seen = {2, 1}
1 != 3
2 in seen yes so skip
dfs(3, 3)
return True
"""
"""
u = 1, v = 2
G[1] = {2}
G[2] = {1}
u = 2 v = 3
G[2] = {1, 3}
G[3] = {2}
u = 3, v = 4
G[3] = {2, 4}
G[4] = {3}
u = 1, v = 4
seen = {}
dfs(1, 4)
1 != 4
seen = {1}
G[1] = {2}
dfs(2, 4)
seen = {1, 2}
2 != 4
G[2] = {1, 3}
1 in seen x
3 not in seen
seen = {1, 2, 3}
dfs(3, 4)
3 != 4
G[3] = {2, 4}
seen = {1, 2, 3}
2 in seen x
4 not in seen
dfs(4, 4) return True
"""
            
