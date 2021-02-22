class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        allCombs = []
        currComb = []
        n = len(word)
        # noNum flag is used to make sure we do not use two nums in succession
        def backtrack(start, noNum): 
            if start == n: # 0, 1
                allCombs.append("".join(currComb))
                return
            nonlocal counter
            for i in range(n+1):
                if i == 0: # i == start
                    currComb.append(word[start]) # ["w"]
                    counter += 1
                    backtrack(start+1, False)
                    currComb.pop()
                elif noNum: return
                else:
                    if i > n - start: break 
                    counter += 1
                    currComb.append(str(i))
                    backtrack(start+i, True)
                    currComb.pop()
                    
        backtrack(0, False)
        return allCombs
