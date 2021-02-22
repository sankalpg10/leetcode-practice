class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
                
        allStates = []
        currState = []
        usedCols = [False]*(2*n-1)
        usedDiags = [False]*(2*n-1)
        usedADiags = [False]*(2*n-1)
        def backtrack(row):
            if row == n:
                allStates.append(generateBoard(currState))
                return
            for col in range(n):
                if isFriendly(row,col):
                    usedCols[col] = True
                    usedDiags[row + col] = True
                    usedADiags[col - row + n - 1] = True
                    currState.append(col)
                    backtrack(row+1)
                    currState.pop()
                    usedCols[col] = False
                    usedDiags[row + col] = False
                    usedADiags[col - row + n - 1] = False
                    
        def generateBoard(state: List[int]) -> List[List[str]]:
            print(state)
            finalPresentation = []
            for currQPos in state:
                currLine = ["."]*n
                currLine[currQPos] = "Q"
                finalPresentation.append("".join(currLine))
                
            return finalPresentation
        
        def isFriendly(row, col):
            if usedCols[col] or usedDiags[row + col] or usedADiags[col - row + n - 1]:
                return False
            return True
            
            
        backtrack(0)
        return allStates
