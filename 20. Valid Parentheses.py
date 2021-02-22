class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parans = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in parans:
                stack.append(char)
            else:
                if not stack: return False
                p = stack.pop()
                if parans[p] != char:
                    return False
            
        return len(stack) == 0
