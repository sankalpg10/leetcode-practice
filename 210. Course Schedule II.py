class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = [[] for _ in range(numCourses)]
        inDegrees = [0 for _ in range(numCourses)]
        for course, preq in prerequisites:
            G[preq].append(course)
            inDegrees[course] += 1
            
        degZeroNodes = []
        for node, indegree in enumerate(inDegrees):
            if indegree == 0:
                degZeroNodes.append(node)
            
        topologicalOrder = []
        while degZeroNodes:
            node = degZeroNodes.pop()
            topologicalOrder.append(node)
            for child in G[node]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    degZeroNodes.append(child)
        
        return topologicalOrder if len(topologicalOrder) == len(G) else []
