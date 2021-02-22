class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        a)b(c)d
        
        """
        
        stack = []
        chars = list(s)
        for i, char in enumerate(chars):
            if char not in "()": continue
            if char == "(":
                stack.append((char, i))
            else:
                if not stack: chars[i] = ""
                else: stack.pop()
            
        while stack:
            _, i = stack.pop()
            chars[i] = ""
        
        return "".join(chars)
