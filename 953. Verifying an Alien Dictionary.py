class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word2Ind = {word: ind for ind, word in enumerate(order)}
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if word2Ind[word1[k]] > word2Ind[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
            
        return True
        
            
        
