class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)
        visited = {"0000"}
        
        def neighbors(currState):
            for wheel in range(4):
                cS = int(currState[wheel])
                for disp in [1, -1]:
                    nS = (cS + disp) % 10
                    yield currState[:wheel] + str(nS) + currState[wheel+1:]
        
        q = collections.deque([('0000', 0)])
        minMoves = inf
        while q:
            currState, totMoves = q.popleft()
            if currState == target: return totMoves
            if currState in deadends: continue
            for nextState in neighbors(currState):
                if nextState not in visited:
                    visited.add(nextState)
                    q.append((nextState, totMoves + 1))
        return -1
