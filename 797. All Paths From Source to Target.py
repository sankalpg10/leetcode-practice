class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def getPaths(graph, currNode, toNode, paths, currpath):
            
            if currpath[-1] == toNode:
                paths.append(currpath)
                return
            
            for child in graph[currNode]:
                
                getPaths(graph, child, toNode, paths, currpath + [child])
                
            
        paths = []
        currpath = [0]
        getPaths(graph, 0, len(graph)-1, paths, currpath)
        return paths
