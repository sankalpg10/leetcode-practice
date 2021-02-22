from heapq import *
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        car:  0   1   2   3   4
        pos: 10   8   0   5   3
        spe:  2   4   1   1   3
        trd:  1   1   12  7   3
        
        time to reach destination (trd) = 12-10/2 = 1  12-8/1 = 1 => (dist(target, pos[j])/speed[j]) >= (dist(target, pos[i])/speed[i]) where i is the car behind j
        
        add (-pos[i], trd[i]) of each car in a maxheap (at the top we would have the trd of the car closest to the target)
        lasttrd = heappop()
        numConvoy = 1
        while heap not empty:
            currtrd = heappop()
            if currtrd < lasttrd:
                numConvoy = 1
            lastrd = currtrd
        
        """
        if len(position) == 0: return 0
        trdheap = [(-pos+1, (target-pos)/spd) for pos, spd in zip(position, speed)] # time to reach destination
        heapify(trdheap)
        
        _, lasttrd = heappop(trdheap)
        numConvoy = 1
        while trdheap:
            _, currtrd = heappop(trdheap)
            if currtrd > lasttrd:
                numConvoy += 1
                lasttrd = currtrd
        
        return numConvoy
