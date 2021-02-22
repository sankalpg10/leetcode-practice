class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = [[] for _ in range(n)]
        for id_, val in enumerate(manager):
            if val != -1:
                G[val].append(id_)
                
        
        def dfs(empID):
            
            maxTimeTaken = 0
            for subord in G[empID]:
                maxTimeTaken = max(maxTimeTaken, dfs(subord))
            
            return informTime[empID] + maxTimeTaken
            

        visited = set()
        return dfs(headID)
