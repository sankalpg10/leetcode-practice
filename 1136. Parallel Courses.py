class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        
        G = [[] for _ in range(N)] # init an adjacency list
        inDegrees = [0]*N # init inDegrees
        for u, v in relations:
            G[u-1].append(v-1) # build adj list from edge list
            inDegrees[v-1] += 1 # add inDegrees
            
        zeroInDeg = collections.deque() # a queue is required for this problem to make sure we take all courses of this sem first
        for node in range(N):
            if inDegrees[node] == 0:
                zeroInDeg.append(node)
        
        totCoursesTaken = 0
        numSems = 0
        while zeroInDeg:
            numSems += 1
            currCourses = len(zeroInDeg)# take all courses this sem
            totCoursesTaken += currCourses
            for i in range(currCourses):
                node = zeroInDeg.popleft()
                for child in G[node]:
                    inDegrees[child] -= 1
                    if inDegrees[child] == 0:
                        zeroInDeg.append(child)
                
        
        return -1 if totCoursesTaken != N else numSems
