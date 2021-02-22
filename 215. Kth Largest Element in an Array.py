from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        def KthLargestMaxHeap():
            heap = []
            for i in range(n):
                if len(heap) < n - k + 1:
                    heappush(heap, -nums[i])
                elif -nums[i] > heap[0]:
                    heappop(heap)
                    heappush(heap, -nums[i])

            return -heap[0]
        
        def KthLargestMinHeap():
            heap = []
            for i in range(len(nums)):
                if len(heap) < k:
                    heappush(heap, nums[i])
                elif nums[i] > heap[0]:
                    heappop(heap)
                    heappush(heap, nums[i])

            return heap[0]
        
        n = len(nums)
        if k > n/2:
            return KthLargestMaxHeap()
        else:
            return KthLargestMinHeap()
