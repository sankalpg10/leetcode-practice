class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        G = [[] for _ in range(n)] # to store graph as a adj list
        inDegrees = [0]*n # to keep track of indegrees of each course
        rG = [set() for _ in range(n)] # inverted graph from a course to its preqrequisites
        for preq, course in prerequisites:
            G[preq].append(course) # convert from edge list to adj list
            inDegrees[course] += 1 # increment indegree of course
            rG[course].add(preq) # add preq to course's preq set
        
        degZeroNodes = [] # get all the nodes with indegree zero
        for preq in range(n):
            if inDegrees[preq] == 0:
                degZeroNodes.append(preq)
                
        while degZeroNodes: # while degZeroNodes is not empty
            preq = degZeroNodes.pop() # pop a zero in degree node from stack
            for course in G[preq]: # for each course which has preq as direct prerequisite add preqrequisites of preq to that course's preq set in reverse Graph rG.
                rG[course] |= rG[preq] # this adds prequisites of preq to prequisites of course. e.g. usage a = {0, 1}, b = {2} a | b = {0, 1, 2}
                inDegrees[course] -= 1 # decrement in degree of the course
                if inDegrees[course] == 0:
                    degZeroNodes.append(course) # add to degZeroNodes stack if indegree of course is 0
        
        return [pre in rG[course] for pre, course in queries]
