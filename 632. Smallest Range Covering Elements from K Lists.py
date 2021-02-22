class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        L = []
        k = len(nums)
        for i, sublist in enumerate(nums):
            for num in sublist:
                L.append((num, i))
            
        L.sort()
        n, l, r = len(L), 0, 0
        sRange = (-inf, inf)
        counts = collections.defaultdict(int)
        zeroCounts = k # num of lists with zero elements
        while True:
            if zeroCounts == 0:
                if sRange[1] - sRange[0] > L[r-1][0] - L[l][0]:
                    sRange = (L[l][0], L[r-1][0])
                counts[L[l][1]] -= 1
                if counts[L[l][1]] == 0: zeroCounts += 1
                l += 1
            else:
                if r == n: break
                counts[L[r][1]] += 1
                if counts[L[r][1]] == 1: zeroCounts -= 1
                r += 1
        
        return sRange
