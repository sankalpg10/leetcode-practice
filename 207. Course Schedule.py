class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G = [[] for _ in range(numCourses)]
        inDegrees = [0 for _ in range(numCourses)]
        for child, parent in prerequisites:
            G[parent].append(child)
            inDegrees[child] += 1

        degZeroNodes = []
        for node, indegree in enumerate(inDegrees):
            if indegree == 0:
                degZeroNodes.append(node)
                
        topOrderedNodes = []
        while degZeroNodes:
            node = degZeroNodes.pop()
            topOrderedNodes.append(node)
            for child in G[node]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    degZeroNodes.append(child)
                    
        return len(topOrderedNodes) == numCourses
