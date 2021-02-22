from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def minHeapSoln():
            hLen = 0
            heap = []
            for i in range(m):
                for j in range(n):
                    if hLen < k:
                        hLen += 1
                        heappush(heap, -matrix[i][j])
                    else:
                        heappush(heap, -matrix[i][j])
                        heappop(heap)
            return -heap[0]
        
        def maxHeapSoln():
            heap = []
            hLen = 0
            for i in range(m):
                for j in range(n):
                    if hLen < m*n - k + 1:
                        hLen += 1
                        heappush(heap, matrix[i][j])
                    else:
                        heappush(heap, matrix[i][j])
                        heappop(heap)
            return heap[0]
        
        m, n = len(matrix), len(matrix[0])
        if k > m*n // 2:
            return maxHeapSoln()
        return minHeapSoln()
