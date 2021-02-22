class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        numReqs = len(requests)
        netMovement = [0]*n
        def netZero():
            for moment in netMovement:
                if moment != 0:
                    return -inf
            return 0
        
        def backtrack(currReq):
            if currReq == numReqs:
                return netZero()
            
            ifSkip = backtrack(currReq+1)
            Out, In = requests[currReq]

            netMovement[In] += 1
            netMovement[Out] -= 1
            ifSkip = max(ifSkip, 1 + backtrack(currReq+1))
            netMovement[Out] += 1
            netMovement[In] -= 1
            return ifSkip
                
        return backtrack(0)
