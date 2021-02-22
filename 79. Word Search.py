class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        L = len(word)
        m, n = len(board), len(board[0])
        if L > m*n: return False
        
        def backtrack(pos, currInd, visited):
            if pos in visited: return False
            if currInd >= L:
                return True
            
            nbrs = ((-1, 0), (0, -1), (1, 0), (0, 1))
            for dx, dy in nbrs:
                nx, ny = pos[0]+dx, pos[1]+dy
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] == word[currInd] and backtrack((nx, ny), currInd+1, visited | {pos}):
                        return True 
            
            return False
    
        for i in range(m):
            for j in range(n):
                visited = set()    
                if word[0] == board[i][j] and backtrack((i, j), 1, visited):
                    return True

        return False
