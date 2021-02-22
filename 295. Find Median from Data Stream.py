from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topHalf = []
        self.botHalf = []
        self.bSize = 0
        self.tSize = 0
        
    def addNum(self, num: int) -> None:
        heappush(self.botHalf, -num)
        
        heappush(self.topHalf, -self.botHalf[0])
        self.tSize += 1
        
        heappop(self.botHalf)
        
        if self.bSize < self.tSize:
            heappush(self.botHalf, -self.topHalf[0])    
            heappop(self.topHalf)
            self.bSize += 1
            self.tSize -= 1
        
    def findMedian(self) -> float:
        if self.bSize > self.tSize: 
            return -self.botHalf[0]
        else: return (-self.botHalf[0] + self.topHalf[0])/2
