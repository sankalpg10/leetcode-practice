class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        uniquePerms = []
        currPerm = []
        valDict = collections.Counter(nums)
        n = len(nums)
        def backtrack():
            if len(currPerm) == n:
                uniquePerms.append(currPerm[:])
                return
            
            for num in valDict:
                if valDict[num] == 0: continue
                valDict[num] -= 1
                currPerm.append(num)
                backtrack()
                currPerm.pop()
                valDict[num] += 1
                
        backtrack()
        return uniquePerms
