class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        if not digits: return []
        n = len(digits)
        mappings = []
        currMapping = []
        def backtrack(currInd):
            if currInd == n:
                mappings.append("".join(currMapping))
                return
            
            for char in digitMap[digits[currInd]]:
                currMapping.append(char)
                backtrack(currInd+1)
                currMapping.pop()
                
        backtrack(0)
        return mappings
