from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key = lambda x: x[0] )
        heap = []
        heappush(heap, intervals[0][1])
        hlen = 1
        numRooms = 1
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            while heap and start >= heap[0]:
                hlen -= 1
                heappop(heap)
            heappush(heap, end)
            hlen += 1
            numRooms = max(numRooms, hlen)
        
        return numRooms
