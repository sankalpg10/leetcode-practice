class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        G = collections.defaultdict(list)
        for w1, w2 in pairs:
            G[w1].append(w2)
            G[w2].append(w1)
            
        for w1, w2 in zip(words1, words2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2: break
                for nbr in G[word]:
                    if nbr not in seen:
                        seen.add(nbr)
                        stack.append(nbr)
                    
            else:
                return False
        return True
