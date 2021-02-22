# Using DFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [None] * n # an array to keep track of whether nodes are safe or not
        
        visited = [False]*n
        def dfs(node):
            if safe[node] != None:
                return safe[node]
            if visited[node]: 
                safe[node] = False
                return False
            
            visited[node] = True
            for child in graph[node]:
                if not dfs(child):
                    safe[node] = False
                    return False
                
            safe[node] = True
            return True
        
        for node in range(n):
            dfs(node)
            
        safenodes = []
        for node in range(n):
            if safe[node]: safenodes.append(node)
                
        return safenodes
    
    # Using Kahn's peel off algorithm topological sort
    class Solution:
        def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
            n = len(graph)
            rgraph = [[] for _ in range(n)]
            for node in range(n):
                for child in graph[node]:
                    rgraph[child].append(node)

            outDegrees = [0]*n
            terminals = []
            for node in range(n):
                outDegrees[node] = len(graph[node])
                if outDegrees[node] == 0:
                    terminals.append(node)

            safenodes = [False]*n
            while terminals:
                node = terminals.pop()
                safenodes[node] = True
                for parent in rgraph[node]:
                    outDegrees[parent] -= 1
                    if outDegrees[parent] == 0:
                        terminals.append(parent)

            return [idx for idx, val in enumerate(safenodes) if val]
