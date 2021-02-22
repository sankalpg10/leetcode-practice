class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        visited = set()
        
        def dfs(ind):
            if arr[ind]==0: return True
            if ind in visited: return False
            visited.add(ind)
            for child in [ind+arr[ind], ind-arr[ind]]:
                if child >= len(arr) or child < 0: continue
                if dfs(child):
                    return True
            return False
        
        return dfs(start)
    
    """
    without a visited set
    
    def canReach(self, arr: List[int], start: int) -> bool:
        
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0: return True
            arr[start] *= -1
            
            return self.dfs(arr, start + arr[start]) or self.dfs(arr, start-arr[start])
            
        return True
    """
        
                
