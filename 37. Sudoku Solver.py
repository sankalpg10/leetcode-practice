class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        numEmpty = 0
        
        def backtrack(currIndex):
            if currIndex == 81:
                return True
            
            row, col = currIndex//9, currIndex%9
            if board[row][col] != ".": 
                return backtrack(currIndex+1)
            
            for k in '123456789':
                if hasConflict(row, col, k): continue
                board[row][col] = k
                if backtrack(currIndex+1): return True
                board[row][col] = "."
                
        def hasConflict(row, col, num):
            
            for i in range(9):
                if board[row][i] == num: return True
                if board[i][col] == num: return True
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == num: return True
                
            return False
        
        backtrack(0)
                    
