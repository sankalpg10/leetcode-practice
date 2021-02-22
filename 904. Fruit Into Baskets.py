class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        n = len(tree)
        baskets = collections.defaultdict(int)
        l, r = 0, 0
        uniFruits = 0
        totFruits = 0
        while r < n:
            if baskets[tree[r]] > 0 or uniFruits < 2:
                baskets[tree[r]] += 1
                uniFruits += baskets[tree[r]] == 1
                r += 1
                totFruits = max(totFruits, r-l)
                
            else:
                baskets[tree[l]] -= 1
                uniFruits -= baskets[tree[l]] == 0
                l += 1
                
        return totFruits
